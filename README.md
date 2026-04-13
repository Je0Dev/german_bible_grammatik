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
│           ├── nomen/           # Das Nomen und seine Begleiter
│           ├── verb/            # Das Verb
│           ├── syntax/          # Satzbau und Syntax
│           ├── praepositionen/  # Präpositionen
│           ├── adjektive/       # Adjektive
│           ├── partikeln/       # Partikeln
│           └── sonstiges/      # Ergänzungen und Anhang
└── output/
    └── master.pdf         # Kompiliertes PDF
```

## Verwendung

### PDF erstellen

```bash
cd grammatik_book
pdflatex -interaction=batchmode master.tex
mv master.pdf output/
```

Das PDF befindet sich dann in `output/master.pdf`.

### PDF mit Hyperlinks

Das erstellte PDF enthält:
- Hyperlinks im Inhaltsverzeichnis
- Verweise zwischen Kapiteln
- Klickbare Querverweise

## Dokumentstruktur

Das Dokument ist in 7 Hauptteile gegliedert:

1. **Teil I: Das Nomen** - Deklination, Artikel, N-Deklination
2. **Teil II: Das Verb** - Zeitformen, Modalverben, Konjunktiv
3. **Teil III: Syntax** - Satzbau, Nebensätze, Passiv
4. **Teil IV: Präpositionen** - Wechselpräpositionen, Kasuspräpositionen
5. **Teil V: Adjektive und Partikeln** - Deklination, Steigerung, Partikeln
6. **Teil VI: Ergänzungen** - Wortstellung, Stolpersteine
7. **Anhang** - Konjugationstabellen, reflexive Verben, Nomenlisten, nützliche Sätze

## Hauptmerkmale

### Farbige Boxen
- ⬜ Blaue Box: Informationen
- ⬜ Rote Box: Warnungen
- ⬜ Gelbe Box: Tipps
- ⬜ Grüne Box: Level-Angaben

### Übungen
Zahlreiche Übungen mit Lösungen:
- Lückentexte
- Umformungsübungen  
- Kasusbestimmung
- Satzbau

### Anhang
- Vollständige Konjugationstabellen
- reflexive Verben mit Präpositionen
- Nomenlisten (m/f/n mit Plural)
- Nützliche Sätze für Meinungen und Optionen
- Nomen/Adjektiv + Präposition Verbindungen

## CEFR-Niveaus

Das Werk deckt alle Niveaus ab:
- **A1** - Grundstufe I
- **A2** - Grundstufe II  
- **B1** - Mittelstufe
- **B2** - Mittelstufe II
- **C1** - Oberstufe

## Quellen

- **Grammatik aktiv B1+/B2/C1** (Jin/Voß) - Cornelsen
- **Lehr- und Übungsbuch der deutschen Grammatik** (Dreyer/Schmitt) - Hueber
- **B-Grammatik** (Buscha/Szita) - Klett
- **Lingolia** - https://deutsch.lingolia.com/de/grammatik

## Lizenz

Dieses Projekt ist für Bildungszwecke erstellt.

---
**Hinweis**: Dieses Werk dient als Ergänzung zum Sprachunterricht.