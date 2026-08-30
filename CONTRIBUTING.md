# Mitmachen und Warten

Dieses Repository hat zwei klar getrennte Rollen:

1. **Vorbereitung** (einmalig, durch Kursverantwortliche):
   Referenzspiel, Kursprüfungen, Prompts, Dokumentation und CI erstellen
   und pflegen.

2. **Lernbetrieb** (dauerhaft, durch die Lernenden):
   Ausschließlich im Verzeichnis `lernprojekt/` arbeiten. GitHub Copilot
   tritt dort nur als Lerncoach auf.

## Grundregeln für Änderungen

- Lösungen gehören **nie** in die Prompts, die Dokumentation oder die
  Kursprüfungen.
- Die Kursprüfungen lesen und führen `lernprojekt/` nur aus. Sie dürfen
  dort keine Dateien anlegen, ändern oder löschen.
- Das Referenzspiel und die Kursprüfungen dürfen niemals aufeinander
  zugreifen.
- Die Datei `lernender-name.txt` ist persönlich und lokal. Sie steht in
  `.gitignore` und darf nie eingecheckt werden.
- Änderungen an `docs/TECHNISCHER-VERTRAG.md` müssen mit den Kursprüfungen
  abgestimmt sein.

## Abweichungen von der geplanten Struktur

Abweichungen von der ursprünglich geplanten Repository-Struktur werden hier
und in `docs/KURSPLAN.md` dokumentiert:

1. Zusätzliche Prompt-Datei `.github/prompts/00-vorbereitung.prompt.md`
   (Phase 0: System einrichten, Name erfragen, Referenzspiel kennenlernen).
2. Lokale Namensdatei `lernender-name.txt` im Wurzelverzeichnis (in
   `.gitignore`). Sie ist die einzige Datei, die Copilot im Lernmodus
   anlegen oder ändern darf (nur der Name, nur mit Zustimmung).
3. `tools/check_lesson.py` unterstützt zusätzlich `--lesson all` für die
   vollständige Basisabnahme.

## Tests

Vor jeder Änderung am Referenzspiel:

```text
cd referenzspiel
python -m unittest discover -s tests
```

Vor jeder Änderung an den Kursprüfungen oder Tools:

```text
python tools/check_lesson.py --lesson all
python tools/validate_repository.py
```
