# tools/ — Werkzeuge für den Kurs

Werkzeuge für Lernende und Kursverantwortliche. Alle Werkzeuge werden
vom Wurzelverzeichnis des Repositories aus gestartet und benutzen
**niemals** das Referenzspiel als Quelle.

| Datei | Zweck | Zielgruppe |
| ----- | ----- | ---------- |
| `check_environment.py` | Prüft Python, virtuelle Umgebung und pygame | Lernende (Phase 0) |
| `check_lesson.py` | Prüft den Stand einer Lektion im Lernprojekt | Lernende, Copilot |
| `validate_repository.py` | Prüft die Vollständigkeit des Repository-Aufbaus | Kursverantwortliche, CI |

## `check_environment.py`

```text
python tools/check_environment.py
```

Läuft auch ohne pygame (nur Standardbibliothek) und sagt genau, was
noch zu tun ist.

## `check_lesson.py`

```text
python tools/check_lesson.py --lesson 1
python tools/check_lesson.py --lesson 7
python tools/check_lesson.py --lesson all
```

Prüft ausschließlich den Stand der gewählten Lektion in `lernprojekt/`.
Ausgabe in Deutsch, eine Zeile pro Anforderung. Exit-Codes:

| Code | Bedeutung |
| ---- | --------- |
| 0    | `BESTANDEN` |
| 1    | `NACHARBEIT ERFORDERLICH` |
| 2    | `NICHT PRÜFBAR` |

`--lesson all` ist die vollständige Basisabnahme (Abweichung von der
ursprünglichen Planung, dokumentiert in `CONTRIBUTING.md`).

## `validate_repository.py`

```text
python tools/validate_repository.py
```

Prüft Struktur, Vollständigkeit der Prompts, die Trennung von
`lernprojekt/` und `referenzspiel/`, den Ausgangszustand des
Lernprojekts und führt die Tests des Referenzspiels aus.

## Regeln für die Kursprüfungen

- Sie dürfen `lernprojekt/` nur lesen und ausführen — niemals verändern.
- Sie prüfen nie Bonusaufgaben und nie spätere Lektionen.
- Sie verraten keine Lösungen.
- Sie funktionieren möglichst ohne geöffnetes pygame-Fenster
  (unsichtbarer Videotreiber).
