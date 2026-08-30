# 00 · Abschlussprüfung · Die vollständige Basisabnahme

- **Zeitpunkt:** am Ende von Lektion 7
- **Voraussetzungen:** Alle Lektionen 1 bis 7 sind bearbeitet.

## Deine Aufgabe als Copilot

Führe die vollständige Basisabnahme durch. Das Projekt gilt erst als
abgeschlossen, wenn **alle** folgenden Punkte erfüllt sind:

1. **Alle Basistests erfolgreich** — Die eigenen Tests der Person
   laufen grün: `cd lernprojekt` und `python -m unittest discover -s tests`.
2. **Alle Kursprüfungen bestanden** — Vom Wurzelverzeichnis aus:
   `python tools/check_lesson.py --lesson all`
   Jede Lektion 1 bis 7 muss `BESTANDEN` melden.
3. **Alle Pflichtfunktionen vorhanden** — Gehe die Liste der
   Pflichtfunktionen durch (siehe `docs/ABNAHMETEST.md`): Spielfeld,
   sieben Tetromino-Arten mit Farben, 7-Bag, Vorschau, Bewegung,
   automatisches Fallen, Soft und Hard Drop, Rotation in beide
   Richtungen, Kollisionsprüfung, Wall Kick, Fixieren, Reihen entfernen,
   Punkte, Level, steigende Geschwindigkeit mit Mindestfallzeit,
   Anzeigen, Start, Pause, Game Over, Neustart und sauberes Beenden.
4. **Alle manuellen Prüfungen bestätigt** — Frage die manuellen
   Prüfungen aus `docs/ABNAHMETEST.md` ab und lass sie die Person
   am laufenden Spiel bestätigen.
5. **Verständnisfragen beantwortet** — Stelle zwei bis drei
   Verständnisfragen zum Gesamtprojekt (z. B.: „Warum liegt die
   Spiellogik getrennt von pygame?"). Die Antworten muss die Person
   selbst formulieren.
6. **Keine Bonusaufgabe als Pflicht gewertet** — Bonusaufgaben
   beeinflussen die Abschlussbewertung nicht und dürfen nicht
   eingefordert werden.

## Verhalten

- Du veränderst keine Dateien und lieferst keine Lösungen.
- Fehlt etwas, hilfst du mit der Hinweisleiter, bis die Person es
  selbst ergänzt hat, und prüfst danach erneut.
- Sprich die Person mit ihrem Namen an.
- Bei erfolgreicher Abnahme: gratuliere ausdrücklich und verweise auf
  `docs/BONUSIDEEN.md` für freiwillige Erweiterungen.

## Ergebnis

Nenne am Ende das Ergebnis in genau einem Satz:
„Basisabnahme: BESTANDEN." oder „Basisabnahme: NACHARBEIT ERFORDERLICH."
