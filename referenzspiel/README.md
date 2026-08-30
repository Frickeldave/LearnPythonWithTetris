# Referenzspiel: Blockfall

> **Wichtiger Hinweis:**
> Dieses Verzeichnis enthält die vollständige Referenzlösung.
> Es wird für die normalen Übungen nicht benötigt.
> Bearbeite deine Aufgaben ausschließlich im Verzeichnis `lernprojekt/`.
>
> Nur in der Vorbereitungsphase (Phase 0) darfst du das Spiel hier
> einmal starten, um es kennenzulernen. Der Code selbst ist für
> Lernende tabu — er verrät dir zu viel.

## Was ist das?

`referenzspiel/` ist die vollständige, funktionierende und getestete
Musterlösung des Spiels „Blockfall“. Sie dient:

- den Kursverantwortlichen als Vorlage und Kontrolle,
- den Lernenden in Phase 0 zum Kennenlernen des Zielspiels,
- der CI-Pipeline als Testobjekt.

Das Referenzspiel ist technisch vollständig von `lernprojekt/` getrennt
und importiert nichts aus dem Lernprojekt.

## Starten

1. In das Verzeichnis wechseln:

   ```text
   cd referenzspiel
   ```

2. Spiel starten:

   ```text
   python main.py
   ```

3. Tests ausführen:

   ```text
   python -m unittest discover -s tests
   ```

## Steuerung

| Taste          | Wirkung                          |
| -------------- | -------------------------------- |
| Pfeil links    | Stein nach links bewegen         |
| Pfeil rechts   | Stein nach rechts bewegen        |
| Pfeil unten    | Soft Drop (weich fallen)         |
| Pfeil oben, X  | im Uhrzeigersinn drehen          |
| Z              | gegen den Uhrzeigersinn drehen   |
| Leertaste      | Hard Drop (sofort fallen lassen) |
| P              | Pause und Fortsetzen             |
| R              | Neustart (auch nach Game Over)   |
| Escape         | Spiel beenden                    |

## Punkte

| Aktion                       | Punkte          |
| ---------------------------- | --------------- |
| 1 Reihe entfernt             | 100 × Level     |
| 2 Reihen entfernt            | 300 × Level     |
| 3 Reihen entfernt            | 500 × Level     |
| 4 Reihen entfernt            | 800 × Level     |
| Soft Drop                    | 1 pro Feld      |
| Hard Drop                    | 2 pro Feld      |

Das Spiel beginnt mit Level 1. Nach jeweils zehn insgesamt entfernten
Reihen steigt das Level, und die Steine fallen schneller. Die Fallzeit
hat einen Mindestwert und wird nie unspielbar schnell.

## Wall Kick

Nach einer Rotation wird zuerst die aktuelle Position geprüft, dann
ein Feld nach links, ein Feld nach rechts und ein Feld nach oben.
Das ist bewusst einfacher als ein offizielles Tetris-Rotationssystem.

## Aufbau

| Datei         | Aufgabe                                       |
| ------------- | --------------------------------------------- |
| `settings.py` | Alle Zahlen, Farben und Einstellungen         |
| `tetromino.py`| Formen, Farben und Rotation der Steine        |
| `board.py`    | Das Spielfeld: Zellen, Kollision, Reihen      |
| `game.py`     | Spiellogik ohne Grafik (gut testbar)          |
| `main.py`     | pygame: Fenster, Eingabe, Zeichnen            |
| `tests/`      | Automatische Tests für die Spiellogik         |

Die Spiellogik (`tetromino.py`, `board.py`, `game.py`) benutzt kein
pygame und funktioniert daher ohne Bildschirm — genau diese Trennung
lernt ihr im Kurs kennen.
