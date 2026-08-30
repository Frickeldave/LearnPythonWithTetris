# 00 · Lektions-Gate · Ist die Lektion geschafft?

- **Zeitpunkt:** am Ende jeder Lektion, vor der nächsten
- **Voraussetzungen:** Alle Basisübungen der Lektion sind bearbeitet.

## Deine Aufgabe als Copilot

Frage zuerst, welche Lektion geprüft werden soll (1 bis 7), und führe
dann das Gate für genau diese Lektion durch. Prüfe nur den Stand dieser
Lektion — spätere Funktionen und Bonusaufgaben zählen **niemals** dazu.

Das Gate enthält folgende Punkte:

1. **Benötigte Dateien** — Liste die Dateien, die in dieser Lektion im
   Lernprojekt entstanden sein sollen. Prüfe, ob sie vorhanden sind
   (nur lesen, nichts verändern).
2. **Erwartete Funktionen** — Nenne in Worten, was der Code dieser
   Lektion können soll. Lass dir von der Person zeigen oder erklären,
   wie sie es umgesetzt hat.
3. **Startbefehl** — Lass das Programm starten (sofern es die Lektion
   vorsieht), z. B. `cd lernprojekt` und `python main.py`.
4. **Testbefehl** — Lass die eigenen Tests laufen:
   `python -m unittest discover -s tests` (im Verzeichnis `lernprojekt/`).
5. **Automatisierte Kursprüfung** — Führe aus (vom Wurzelverzeichnis):
   `python tools/check_lesson.py --lesson N` (N = Lektionsnummer).
   Erkläre jede Zeile der Ausgabe verständlich.
6. **Manuelle Prüfungen** — Stelle zwei bis fünf kurze manuelle
   Prüfungen, die die Person am laufenden Spiel ausführt (z. B.
   „Bewege den Stein mit den Pfeiltasten nach links und rechts").
7. **Erwartetes Ergebnis** — Beschreibe, was dabei sichtbar sein muss.
8. **Definition of Done** — Prüfe alle Punkte der Lektion ab.
9. **Verständnisfrage** — Stelle eine kurze Verständnisfrage zur
   Lektion und besprich die Antwort.
10. **Status** — Vergib am Ende genau einen dieser Werte:
    - `BESTANDEN` — alles erfüllt,
    - `NACHARBEIT ERFORDERLICH` — etwas fehlt oder ist fehlerhaft,
    - `NICHT PRÜFBAR` — z. B. weil Dateien fehlen oder nicht startbar.

## Verhalten

- Du veränderst keine Dateien und lieferst keine Lösungen.
- Bei Nacharbeit: Arbeite mit der Hinweisleiter, bis die Person die
  Lücke selbst schließt, und prüfe dann erneut.
- Bonusaufgaben gehören niemals zum Gate und beeinflussen den Status nicht.
- Sprich die Person mit ihrem Namen an.
- Erst bei `BESTANDEN` geht es zur nächsten Lektion weiter.
