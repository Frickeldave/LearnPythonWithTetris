# Abnahmetest: Die vollständige Basisabnahme

Dieser Test wird am Ende von Lektion 7 durchgeführt (Prompt
`00-abschlusspruefung.prompt.md`). Das Projekt gilt erst als
abgeschlossen, wenn **alle** Punkte erfüllt sind.

## 1. Automatische Prüfungen

Im Verzeichnis `lernprojekt/`:

```text
python -m unittest discover -s tests
```

Ergebnis: alle eigenen Tests grün (`OK`).

Vom Wurzelverzeichnis:

```text
python tools/check_lesson.py --lesson all
```

Ergebnis: alle Lektionen 1 bis 7 melden `BESTANDEN`.

## 2. Pflichtfunktionen (am laufenden Spiel prüfen)

- [ ] Spielfeld mit 10 Spalten und 20 sichtbaren Reihen
- [ ] alle sieben Tetromino-Arten mit eigener Farbe
- [ ] faire Zufallsreihenfolge (7-Bag)
- [ ] Vorschau auf den nächsten Stein
- [ ] Bewegung nach links und rechts
- [ ] automatisches Fallen mit steigender Geschwindigkeit und Mindestfallzeit
- [ ] Soft Drop (1 Punkt pro Feld)
- [ ] Hard Drop (2 Punkte pro Feld)
- [ ] Rotation in beide Richtungen mit vereinfachtem Wall Kick
- [ ] Kollisionsprüfung gegen Wände und belegte Zellen
- [ ] Fixieren gelandeter Steine
- [ ] Erkennen und Entfernen vollständiger Reihen
- [ ] Punkteberechnung (100/300/500/800 × Level)
- [ ] Zählen entfernter Reihen und Levelsystem (alle 10 Reihen +1)
- [ ] Anzeige von Punkten, Level und Reihen
- [ ] Startzustand und Neustart ohne Schließen des Programms
- [ ] Pause und Fortsetzen
- [ ] Game-Over-Erkennung und Anzeige
- [ ] sauberes Beenden (X und Escape)

## 3. Manuelle Prüfungen

1. **Start:** Das Spiel öffnet sich mit Fenstertitel, Spielfeld,
   aktivem Stein und Vorschau.
2. **Bewegung:** Der Stein bewegt sich mit den Pfeiltasten genau eine
   Spalte pro Druck und bleibt an den Rändern stehen.
3. **Stapel:** Zwei Steine stapeln sich ohne Überlappung; der zweite
   bleibt auf dem ersten stehen.
4. **Reihen:** Eine vollständige Reihe verschwindet; der Stapel rutscht
   nach; Punkte und Reihenzähler steigen.
5. **Pause und Game Over:** P friert das Spiel ein; bei blockierter
   Startzone erscheint „GAME OVER"; R startet neu.

## 4. Verständnisfragen (selbst beantworten)

1. Warum liegt die Spiellogik getrennt von pygame?
2. Was passiert beim Fixieren eines Steins — in deinen eigenen Worten?
3. Warum hat die Fallzeit einen Mindestwert?

## Bewertung

- `BESTANDEN`: alle Punkte erfüllt.
- `NACHARBEIT ERFORDERLICH`: mindestens ein Punkt offen.

Bonusaufgaben werden **niemals** Teil der Abnahme.
