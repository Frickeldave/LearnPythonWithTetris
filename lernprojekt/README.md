# lernprojekt/ — dein Arbeitsbereich

Hier entsteht **dein** Blockfall-Spiel. Du schreibst jede Zeile
Python-Code selbst. GitHub Copilot hilft dir dabei nur als Lehrer —
er schreibt und verändert hier keine Dateien.

> Diese README darfst du im Laufe des Kurses durch deine eigene
> Projektbeschreibung ersetzen (Lektion 7).

## Was hier entsteht

Im Laufe des Kurses erstellst du in diesem Verzeichnis mindestens:

| Datei           | Aufgabe                                  | Lektion |
| --------------- | ---------------------------------------- | ------- |
| `main.py`       | pygame: Fenster, Eingabe, Zeichnen       | 1       |
| `settings.py`   | Zahlen, Farben und Einstellungen         | 1       |
| `tetromino.py`  | Formen, Farben und Rotation der Steine   | 2       |
| `board.py`      | Das Spielfeld: Zellen und Kollision      | 3       |
| `game.py`       | Spiellogik ohne Grafik                   | 4       |
| `tests/`        | Deine eigenen automatischen Tests        | 3–7     |
| `README.md`     | Deine eigene Projektbeschreibung         | 7       |

## Regeln für diesen Bereich

1. Arbeite ausschließlich hier — nicht in `referenzspiel/`.
2. Kopiere keine fertigen Lösungen; das Lernziel ist dein eigener Weg.
3. Benutze Copilot mit der Hinweisleiter: erst Leitfrage, dann Hinweis,
   dann Pseudocode — niemals fertigen Code.
4. Prüfe deinen Fortschritt regelmäßig:
   - eigene Tests: `python -m unittest discover -s tests`
   - Kursprüfung: `python ../tools/check_lesson.py --lesson 1` (Zahl
     an die aktuelle Lektion anpassen)

## Reihenfolge

Beginne mit dem Prompt `00-kurs-start.prompt.md` in `.github/prompts/`
und arbeite dich dann Übung für Übung durch `L01` bis `L07`.

Viel Spaß — und viel Erfolg!
