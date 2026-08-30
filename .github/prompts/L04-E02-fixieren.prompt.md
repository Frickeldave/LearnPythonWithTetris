# L04 · E02 · Fixieren

- **Lektion:** 4
- **Übung:** 2 von 4
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 25 Minuten
- **Voraussetzungen:** Übung 1 bestanden
- **Lernziel:** Ein gelandeter Stein wird ins Spielfeld eingetragen
  (fixiert), und sofort erscheint der nächste Stein.
- **Sichtbares Ergebnis:** Steine stapeln sich unten; der nächste Stein
  erscheint automatisch oben.
- **Betroffene Dateien:** `lernprojekt/main.py`, `lernprojekt/board.py`
- **Wichtige Begriffe:** Fixieren, Eintragen ins Gitter, nächster Stein

## Aufgabe in kleinen Schritten

1. Erkenne den Moment, in dem der Stein nicht weiter nach unten kann.
2. Trage dann alle Zellen des Steins mit seiner Farbe ins Spielfeld ein.
3. Mache anschließend den nächsten Stein aktiv und bestimme den
  übernächsten (Vorschau aus Lektion 2).
4. Prüfe: Kein Stein bleibt „in der Luft" hängen, keiner überlappt
  einen anderen.
5. Beobachte, was passiert, wenn ein neuer Stein sofort blockiert ist —
  das behandelst du später genauer (Game Over, Lektion 6).

## Unterstützung

- **Erlaubt:** Copilot erklärt den Übergang „aktiv → fixiert → nächster".
- **Verboten:** Keine fertige Fixier-Funktion.

## Prüfen

**Manuell:** Steine stapeln sich korrekt; der nächste Stein startet
immer oben; keine Überlappungen.

## Erwartetes Ergebnis

Gelandete Steine werden Teil des Spielfelds, und das Spiel läuft mit
dem nächsten Stein weiter.

## Definition of Done

- [ ] Ein Stein, der nicht weiter fallen kann, wird ins Gitter eingetragen.
- [ ] Die Zellen speichern die Farbe des Steins.
- [ ] Danach wird automatisch der nächste Stein aktiv.
- [ ] Es entstehen keine Überlappungen.

## Verständnisfrage

Warum gehört ein fixierter Stein danach zum Spielfeld statt zum
aktiven Stein?

## Hinweisleiter

1. **Leitfrage:** Was unterscheidet einen fallenden von einem
   gelandeten Stein?
2. **Konzeptueller Hinweis:** Der fallende Stein ist beweglich; der
   gelandete wird zu festen Zellen im Gitter.
3. **Algorithmus in Worten:** Fallen scheitert → Zellen eintragen →
   nächsten Stein aktivieren.
4. **Pseudocode:** wenn nicht fallen möglich: fixieren; nächster Stein.
5. **Beispiel (max. 5 Zeilen):** Schleife, die Zellen in eine Liste schreibt.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L04-E03-rotation.prompt.md`.
