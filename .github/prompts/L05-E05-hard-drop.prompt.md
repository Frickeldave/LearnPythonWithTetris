# L05 · E05 · Hard Drop

- **Lektion:** 5
- **Übung:** 5 von 5
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 20 Minuten
- **Voraussetzungen:** Übung 4 bestanden
- **Lernziel:** Mit der Leertaste fällt der Stein sofort ganz nach
  unten, wird fixiert — und bringt Punkte pro gefallenem Feld.
- **Sichtbares Ergebnis:** Leertaste lässt den Stein augenblicklich
  landen; 2 Punkte pro überflogenem Feld.
- **Betroffene Dateien:** `lernprojekt/main.py`, `lernprojekt/game.py`
- **Wichtige Begriffe:** Hard Drop, Schleife bis zum Boden, Fixieren

## Aufgabe in kleinen Schritten

1. Erkenne die Leertaste als Tastendruck.
2. Wiederhole den Fallschritt, bis er nicht mehr möglich ist — und
  zähle die Schritte mit.
3. Gib 2 Punkte pro gefallenem Feld.
4. Fixiere den Stein anschließend genau wie bei der Schwerkraft.
5. Teste aus großer Höhe und direkt über dem Boden.

## Unterstützung

- **Erlaubt:** Copilot erklärt Schleifen mit Abbruchbedingung.
- **Verboten:** Keine fertige Hard-Drop-Funktion.

## Prüfen

**Manuell:** Leertaste lässt den Stein sofort landen; die Punktzahl
steigt um 2 × Fallstrecke; danach kommt der nächste Stein.

## Erwartetes Ergebnis

Hard Drop mit korrekter Punktzahl und anschließendem Fixieren.

## Definition of Done

- [ ] Leertaste löst den Hard Drop aus.
- [ ] Der Stein fällt in einem Rutsch bis zum Boden.
- [ ] Jedes überflogene Feld bringt 2 Punkte.
- [ ] Danach wird der Stein fixiert und der nächste aktiviert.

## Verständnisfrage

Worin unterscheiden sich Soft Drop und Hard Drop — und warum bringt
Hard Drop mehr Punkte?

## Hinweisleiter

1. **Leitfrage:** Wie lässt du einen Schritt so oft wiederholen, bis
  er scheitert?
2. **Konzeptueller Hinweis:** Eine Schleife mit Zähler wiederholt den
  Fallschritt; die Abbruchbedingung ist die Kollisionsprüfung.
3. **Algorithmus in Worten:** solange fallen möglich: fallen und zählen;
  dann Punkte vergeben und fixieren.
4. **Pseudocode:** solange Schritt klappt: abstand += 1; danach fixieren.
5. **Beispiel (max. 5 Zeilen):** `while`-Schleife mit Zähler.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Lektion 5 ist komplett: Lektions-Gate mit `00-lektions-gate.prompt.md`.
