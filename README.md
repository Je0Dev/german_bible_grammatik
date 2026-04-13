# Deutsche Grammatik A1-C - Kompendium

Ein umfassendes Grammatik-Nachschlagewerk für deutsche Sprache von A1 bis C1-Niveau.

## Ordnerstruktur

```
grammatik_book/
├── README.md              # Diese Dokumentation
├── master.tex             # Haupt-LaTeX-Datei
├── tex/
│   └── input/
│       └── grammatik/
│           ├── a1/             # A1 Grundlagen
│           ├── b1b2/           # B1-B2 Mittelstufe
│           ├── c1/             # C1 Oberstufe
│           ├── nomen/          # Das Nomen
│           ├── verb/           # Das Verb (inkl. Verben mit Objekten)
│           ├── syntax/        # Satzbau und Syntax
│           ├── praepositionen/ # Präpositionen
│           ├── adjektive/     # Adjektive
│           ├── partikeln/      # Partikeln
│           └── sonstiges/    # Ergänzungen, Meinungen, Nomen-Guide
└── output/
    └── master.pdf         # Kompiliertes PDF (472KB)
```

## Verwendung

### PDF erstellen

```bash
cd grammatik_book
pdflatex master.tex
mv master.pdf output/
```

### Inhaltsübersicht

Das Dokument enthält:

- **A1-A2**: Grundlagen (Wortstellung, Präsens, Perfekt, Artikel)
- **B1**: Mittelstufe (Nebensätze, Passiv, Konjunktiv)
- **B2-C1**: Fortgeschritten (Nominalstil, Partizipien, komplexe Sätze)
- **Anhang**: Konjugationstabellen, Meinungsäußerungen, Nomen-Guide (der/die/das), Verben mit Kasus

## Hauptmerkmale

- Farbcodierte CEFR-Niveaus (A1-C1)
- Umfangreiche Übungen mit Lösungen
- Konjugationstabellen
- Nomen-Guide mit Pluralformen
- Verben mit Akkusativ, Dativ und beiden Fällen
- SSM-style Ausdruckssammlung für Meinungen und Argumente

## Quellen

- Grammatik aktiv B1+/B2/C1 (Jin/Voß) - Cornelsen
- Lehr- und Übungsbuch der deutschen Grammatik (Dreyer/Schmitt)
- B-Grammatik (Buscha/Szita) - Klett
- Lingolia - deutsch.lingolia.com/de/grammatik
- SSM Training Materialien

## Copyright

Copyright © 2026 - George Mastro

GitHub: github.com/Je0Dev

---
**Hinweis**: Dieses Werk dient als Ergänzung zum Sprachunterricht.