# Kursplan: Blockfall in einer Woche

Der Kurs ist auf **sieben Lektionen** ausgelegt — ungefähr eine Lektion
pro Tag. Pro Lektion sind **75 bis 105 Minuten Basiszeit** geplant,
insgesamt höchstens **zwölf Stunden**. Bonusaufgaben zählen nicht zur
Basiszeit.

Das Basisspiel ist am Ende von **Lektion 6** vollständig spielbar.
Lektion 7 dient dem Testen, Aufräumen, Dokumentieren und der
Abschlussprüfung.

## Phase 0: Vorbereitung (vor Lektion 1)

| Dauer | Inhalt |
| ----- | ------ |
| ca. 45–60 Min | System einrichten (Python, venv, pygame), Name erfragen, Referenzspiel einmal starten und kennenlernen |

Die Vorbereitung zählt **nicht** zur zwölfstündigen Basiszeit.

## Die sieben Lektionen

| Lektion | Thema | Übungen (Basis) | Zeit |
| ------- | ----- | --------------- | ---- |
| 1 | Fenster, Event-Loop, Spielfeld | E01–E05 | ca. 95 Min |
| 2 | Tetrominos, aktiver Stein, 7-Bag, Vorschau | E01–E05 | ca. 95 Min |
| 3 | Bewegung, Grenzen, belegte Zellen, erste Tests | E01–E04 | ca. 90 Min |
| 4 | Schwerkraft, Fixieren, Rotation, Wall Kick | E01–E04 | ca. 95 Min |
| 5 | Reihen, Punkte, Level, Soft/Hard Drop | E01–E05 | ca. 100 Min |
| 6 | Anzeige, Pause, Game Over, Neustart, Hinweise | E01–E05 | ca. 90 Min |
| 7 | Tests, Aufräumen, README, Abnahme | E01–E04 | ca. 100 Min |

Nach jeder Lektion folgt ein **Lektions-Gate** (`00-lektions-gate.prompt.md`,
ca. 15 Minuten).

## Bonusaufgaben

Bonusaufgaben (Dateinamen mit `B`) sind freiwillig:

- Sie beginnen erst nach bestandener Basislektion.
- Sie sind keine Voraussetzung für spätere Übungen.
- Sie dürfen jederzeit übersprungen werden.
- Sie zählen nicht zur Basiszeit.
- Sie beeinflussen die Abschlussbewertung nicht.

## Abweichungen von der ursprünglichen Planung

1. Es gibt eine zusätzliche **Phase 0 (Vorbereitung)** mit dem Prompt
   `00-vorbereitung.prompt.md`.
2. Der Name der lernenden Person steht in der lokalen Datei
   `lernender-name.txt` (Wurzelverzeichnis, in `.gitignore`).
3. `tools/check_lesson.py` unterstützt `--lesson all` für die
   vollständige Basisabnahme.
