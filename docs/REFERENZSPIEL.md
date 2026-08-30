# Referenzspiel: Hinweise für Kursverantwortliche

Dieses Dokument beschreibt das Referenzspiel aus Sicht der
Kursverantwortlichen. Lernende brauchen es nicht — für sie gilt der
Hinweis in `referenzspiel/README.md`.

## Zweck

`referenzspiel/` ist die vollständige, funktionierende und getestete
Referenzimplementierung des Blockfall-Kurses:

- Sie beweist, dass das Kursziel in der geplanten Zeit erreichbar ist.
- Sie dient als Vergleich bei der Wartung der Kursprüfungen.
- Die Lernenden starten sie einmal in Phase 0, um das Ziel kennenzulernen.
- Die CI führt ihre Tests bei jedem Push aus.

## Wichtige Trennungsregeln

- Das Referenzspiel importiert **nichts** aus `lernprojekt/`.
- Die Kursprüfungen (`course_checks/`) importieren **nichts** aus
  `referenzspiel/`.
- Copilot darf das Verzeichnis im Lernmodus weder lesen noch durchsuchen.

## Enthaltene Funktionen

Spielfeld (10 × 20), alle sieben Tetromino-Arten mit eigenen Farben,
7-Bag-System, Vorschau, Bewegung, automatisches Fallen, Soft Drop,
Hard Drop, Rotation in beide Richtungen, Kollisionsprüfung,
vereinfachter Wall Kick, Fixieren, Reihen erkennen/entfernen,
Punkte (100/300/500/800 × Level, 1 bzw. 2 Punkte pro Feld), Reihen-
und Levelzähler (alle 10 Reihen +1 Level), Mindestfallzeit, Anzeigen,
Startzustand, Pause, Game-Over-Erkennung, Neustart (R), sauberes
Beenden (Esc), Tests der zentralen Spiellogik, Bedienungsdokumentation.

Das Spiel kommt ohne externe Bilder, Schriftarten oder Sounds aus —
alles wird mit pygame gezeichnet.

## Starten und testen

```text
cd referenzspiel
python main.py
```

```text
python -m unittest discover -s tests
```

## Struktur

- `settings.py`: Zahlen und Farben
- `tetromino.py`: Formen, Farben, Rotation
- `board.py`: Zellen, Kollision, Reihen
- `game.py`: Spiellogik ohne pygame
- `main.py`: pygame-Darstellung und Eingabe
- `tests/`: Tests für die Spiellogik

## Wall Kick

Nach einer Rotation prüft das Spiel die aktuelle Position, dann ein
Feld nach links, ein Feld nach rechts und ein Feld nach oben. Das ist
bewusst einfacher als ein offizielles Tetris-Rotationssystem.

## Wartung

Änderungen hier sind Teil der einmaligen Repository-Vorbereitung oder
einer ausdrücklich beauftragten administrativen Wartung — nie Teil des
Lernbetriebs. Nach jeder Änderung: Tests ausführen und
`tools/validate_repository.py` laufen lassen.
