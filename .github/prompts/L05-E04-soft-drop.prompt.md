# L05 · E04 · Soft Drop

- **Lektion:** 5
- **Übung:** 4 von 5
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 15 Minuten
- **Voraussetzungen:** Übung 3 bestanden
- **Lernziel:** Mit Pfeil unten fällt der Stein gezielt ein Feld nach
  unten — und sammelt Punkte.
- **Sichtbares Ergebnis:** Jeder Druck auf Pfeil unten senkt den Stein
  ein Feld und gibt 1 Punkt.
- **Betroffene Dateien:** `lernprojekt/main.py`, `lernprojekt/game.py`
- **Wichtige Begriffe:** Soft Drop, manuelles Fallen, Punkte pro Feld

## Aufgabe in kleinen Schritten

1. Reagiere auf Pfeil unten mit einem Fallschritt („erst prüfen, dann bewegen").
2. Zähle 1 Punkt pro erfolgreich gefallenem Feld.
3. Setze danach den Schwerkraft-Takt zurück, damit der Stein nicht
  direkt doppelt fällt.
4. Unterscheide bewusst: manuelles Fallen gibt Punkte, automatisches nicht.

## Unterstützung

- **Erlaubt:** Copilot erklärt den Unterschied zwischen manuellem und
  automatischem Fallen.
- **Verboten:** Keine fertige Soft-Drop-Funktion.

## Prüfen

**Manuell:** Pfeil unten senkt den Stein ein Feld und erhöht die
Punktzahl um 1; am Boden passiert nichts (keine negativen Effekte).

## Erwartetes Ergebnis

Soft Drop mit 1 Punkt pro Feld und sauberem Zusammenspiel mit der Schwerkraft.

## Definition of Done

- [ ] Pfeil unten löst einen Fallschritt aus.
- [ ] Jeder erfolgreiche Schritt bringt 1 Punkt.
- [ ] Der Schwerkraft-Takt wird danach neu begonnen.
- [ ] Am Boden ändert sich nichts (auch keine Punkte).

## Verständnisfrage

Warum muss nach einem Soft Drop der Schwerkraft-Takt neu starten?

## Hinweisleiter

1. **Leitfrage:** Was passiert, wenn Soft Drop und Schwerkraft
  gleichzeitig „einen Schritt" auslösen?
2. **Konzeptueller Hinweis:** Beide nutzen denselben Fallschritt —
  deshalb den Zeitmesser nach manuellem Fallen zurücksetzen.
3. **Algorithmus in Worten:** Taste erkennen, Schritt versuchen, bei
  Erfolg Punkt vergeben und Takt zurücksetzen.
4. **Pseudocode:** wenn Schritt nach unten klappt: punkte += 1; timer = 0.
5. **Beispiel (max. 5 Zeilen):** Bedingung mit Zähler-Erhöhung.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L05-E05-hard-drop.prompt.md`.
