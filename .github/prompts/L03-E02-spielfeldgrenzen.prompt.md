# L03 · E02 · Spielfeldgrenzen

- **Lektion:** 3
- **Übung:** 2 von 4
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 20 Minuten
- **Voraussetzungen:** Übung 1 bestanden
- **Lernziel:** Dein Stein bleibt innerhalb des Spielfelds — er prallt
  an den Wänden ab, statt zu verschwinden.
- **Sichtbares Ergebnis:** Der Stein lässt sich nicht über den linken
  oder rechten Rand hinaus bewegen.
- **Betroffene Dateien:** `lernprojekt/main.py` (Logik darf gern in
  eine eigene Datei wandern)
- **Wichtige Begriffe:** Grenze, Bedingung, Kollision

## Aufgabe in kleinen Schritten

1. Überlege: Welche x-Werte sind für die Zellen des Steins erlaubt?
2. Prüfe vor jedem Schritt, ob der Stein nach der Bewegung noch
   vollständig im Feld liegt.
3. Bewege den Stein nur, wenn die Prüfung erfolgreich ist.
4. Teste beide Ränder gründlich — auch mit dem breiten I-Stein.

## Unterstützung

- **Erlaubt:** Copilot erklärt, warum man „erst prüfen, dann bewegen" sollte.
- **Verboten:** Keine fertige Prüffunktion.

## Prüfen

**Manuell:** An beiden Rändern bleibt der Stein vollständig sichtbar
stehen, egal wie oft du die Taste drückst.

## Erwartetes Ergebnis

Bewegung stoppt exakt an den Spielfeldgrenzen.

## Definition of Done

- [ ] Vor jeder Bewegung wird geprüft, ob sie erlaubt ist.
- [ ] Der Stein kann das Feld links nicht verlassen.
- [ ] Der Stein kann das Feld rechts nicht verlassen.
- [ ] Alle Zellen des Steins — nicht nur der Mittelpunkt — bleiben drin.

## Verständnisfrage

Warum reicht es nicht, nur die Position des Steins zu prüfen, statt
jede einzelne Zelle?

## Hinweisleiter

1. **Leitfrage:** Welche Spaltennummer hat die Zelle ganz links in
   einem 10 Spalten breiten Feld?
2. **Konzeptueller Hinweis:** „Erst prüfen, dann bewegen" verhindert
   ungültige Zustände.
3. **Algorithmus in Worten:** neue Position berechnen; wenn alle Zellen
   gültig sind, Position übernehmen.
4. **Pseudocode:** wenn jede Zelle innerhalb des Feldes: bewegen.
5. **Beispiel (max. 5 Zeilen):** Bedingung mit `if` und Bereichsprüfung.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L03-E03-belegte-zellen.prompt.md`.
