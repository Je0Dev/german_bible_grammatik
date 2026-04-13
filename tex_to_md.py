#!/usr/bin/env python3
"""
Tex to Markdown Converter
Converts German Grammar LaTeX files to Markdown format
"""

import os
import re
import sys
from pathlib import Path


class TexToMarkdown:
    def __init__(self):
        self.output_dir = "markdown_output"
        self.ignore_patterns = [
            r"\\documentclass",
            r"\\usepackage",
            r"\\geometry",
            r"\\definecolor",
            r"\\hypersetup",
            r"\\titleformat",
            r"\\newtcolorbox",
            r"\\makeatletter",
            r"\\makeatother",
            r"\\pagestyle",
            r"\\fancyhf",
            r"\\rhead",
            r"\\lhead",
            r"\\rfoot",
            r"\\begin\{document\}",
            r"\\end\{document\}",
            r"\\maketitle",
            r"\\tableofcontents",
            r"\\newpage",
            r"\\part\{",
            r"\\mainmatter",
            r"\\frontmatter",
            r"\\backmatter",
            r"\\input\{",
            r"\\chapterend",
            r"\\columnsep",
            r"\\司",
        ]

    def process_file(self, filepath):
        """Process a single .tex file and return markdown content"""
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Apply transformations
        content = self.remove_ignored_patterns(content)
        content = self.convert_chapters(content)
        content = self.convert_sections(content)
        content = self.convert_subsections(content)
        content = self.convert_bold_italics(content)
        content = self.convert_emphasis(content)
        content = self.convert_lists(content)
        content = self.convert_tables(content)
        content = self.convert_boxes(content)
        content = self.convert_links(content)
        content = self.clean_special_chars(content)

        return content

    def remove_ignored_patterns(self, content):
        """Remove LaTeX commands that shouldn't appear in output"""
        for pattern in self.ignore_patterns:
            content = re.sub(pattern, "", content)
        return content

    def convert_chapters(self, content):
        """Convert \chapter to # heading"""
        content = re.sub(r"\\chapter\{([^}]+)\}", r"## \1\n\n", content)
        return content

    def convert_sections(self, content):
        """Convert \section to ## heading"""
        content = re.sub(r"\\section\{([^}]+)\}", r"### \1\n\n", content)
        return content

    def convert_subsections(self, content):
        """Convert \subsection to #### heading"""
        content = re.sub(r"\\subsection\{([^}]+)\}", r"#### \1\n\n", content)
        return content

    def convert_bold_italics(self, content):
        """Convert bold and italic commands"""
        # \textbf{...} -> **...**
        content = re.sub(r"\\textbf\{([^}]+)\}", r"**\1**", content)
        # \textit{...} -> *...*
        content = re.sub(r"\\textit\{([^}]+)\}", r"*\1*", content)
        # \emph{...} -> *...*
        content = re.sub(r"\\emph\{([^}]+)\}", r"*\1*", content)
        return content

    def convert_emphasis(self, content):
        """Convert color and underline commands"""
        # \textcolor{color}{text} -> text (with note)
        content = re.sub(r"\\textcolor\{[^}]+\}\{([^}]+)\}", r"\1", content)
        # \underline{text} -> <u>text</u>
        content = re.sub(r"\\underline\{([^}]+)\}", r"<u>\1</u>", content)
        return content

    def convert_lists(self, content):
        """Convert itemize and enumerate environments"""
        # itemize -> markdown lists
        content = re.sub(r"\\begin\{itemize\}", "\n", content)
        content = re.sub(r"\\end\{itemize\}", "\n", content)
        content = re.sub(r"\\begin\{enumerate\}", "\n", content)
        content = re.sub(r"\\end\{enumerate\}", "\n", content)
        content = re.sub(r"\\item\s*", "- ", content)
        return content

    def convert_tables(self, content):
        """Convert tabular environments to markdown tables"""
        # This is a simplified conversion - more complex tables need manual editing
        content = re.sub(r"\\begin\{center\}", "", content)
        content = re.sub(r"\\end\{center\}", "", content)
        content = re.sub(r"\\begin\{tabular\}", "", content)
        content = re.sub(r"\\end\{tabular\}", "", content)
        content = re.sub(r"\\hline", "|", content)
        content = re.sub(r"\\\\\s*", "|\n", content)
        content = re.sub(r"\&", "|", content)
        return content

    def convert_boxes(self, content):
        """Convert tcolorbox to blockquotes or headers"""
        content = re.sub(
            r"\\begin\{infobox\}.*?\{([^}]+)\}(.*?)\\end\{infobox\}",
            r"**INFO:** \1\n\2",
            content,
            flags=re.DOTALL,
        )
        content = re.sub(
            r"\\begin\{warnbox\}.*?\{([^}]+)\}(.*?)\\end\{warnbox\}",
            r"**WARNUNG:** \1\n\2",
            content,
            flags=re.DOTALL,
        )
        content = re.sub(
            r"\\begin\{tippbox\}.*?\{([^}]+)\}(.*?)\\end\{tippbox\}",
            r"**TIPP:** \1\n\2",
            content,
            flags=re.DOTALL,
        )
        return content

    def convert_links(self, content):
        """Convert hyperref links"""
        content = re.sub(r"\\href\{([^}]+)\}\{([^}]+)\}", r"[\2](\1)", content)
        return content

    def clean_special_chars(self, content):
        """Clean up special LaTeX characters"""
        content = re.sub(r"\\%", "%", content)
        content = re.sub(r"\\$", "$", content)
        content = re.sub(r"\\&", "&", content)
        content = re.sub(r"#", "#", content)
        content = re.sub(r"_", "_", content)
        content = re.sub(r"\{", "", content)
        content = re.sub(r"\}", "", content)
        content = re.sub(r"~", " ", content)
        # Clean up multiple newlines
        content = re.sub(r"\n{3,}", "\n\n", content)
        return content

    def convert_directory(self, input_dir, output_dir=None):
        """Convert all .tex files in directory to markdown"""
        if output_dir is None:
            output_dir = self.output_dir

        # Create output directory
        os.makedirs(output_dir, exist_ok=True)

        tex_files = list(Path(input_dir).rglob("*.tex"))
        print(f"Found {len(tex_files)} .tex files")

        for tex_file in tex_files:
            try:
                # Get relative path to maintain structure
                rel_path = tex_file.relative_to(input_dir)
                output_path = Path(output_dir) / rel_path.with_suffix(".md")

                # Create parent directories
                output_path.parent.mkdir(parents=True, exist_ok=True)

                # Process file
                md_content = self.process_file(tex_file)

                # Add header
                header = f"""---
title: {rel_path.stem}
description: German Grammar Reference
---

"""
                md_content = header + md_content

                # Write output
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(md_content)

                print(f"✓ Converted: {rel_path} -> {output_path}")

            except Exception as e:
                print(f"✗ Error processing {tex_file}: {e}")

        print(f"\nConversion complete! Output in: {output_dir}/")


def main():
    if len(sys.argv) > 1:
        input_dir = sys.argv[1]
    else:
        input_dir = "tex/input/grammatik"

    if len(sys.argv) > 2:
        output_dir = sys.argv[2]
    else:
        output_dir = "markdown_output"

    converter = TexToMarkdown()
    converter.convert_directory(input_dir, output_dir)


if __name__ == "__main__":
    main()
