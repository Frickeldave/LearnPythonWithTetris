# L02 · E01 · Tetrominos beschreiben

- **Lektion:** 2
- **Übung:** 1 von 5
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 15 Minuten
- **Voraussetzungen:** Lektion 1 bestanden
- **Lernziel:** Du beschreibst alle sieben Tetromino-Arten als Daten
  in deinem Programm.
- **Sichtbares Ergebnis:** Das Terminal zeigt für jede Art ihre Form
  und Anzahl der Zellen.
- **Betroffene Dateien:** `lernprojekt/tetromino.py`
- **Wichtige Begriffe:** Datenstruktur, Wörterbuch, Liste, Zeichenkette

## Aufgabe in kleinen Schritten

1. Lege die Datei `tetromino.py` an.
2. Überlege: Wie beschreibst du eine Form aus Zellen mit Text?
3. Lege ein Wörterbuch an, das für jede Art (I, O, T, S, Z, J, L)
   eine Form enthält.
4. Prüfe im Terminal, dass jede Art genau vier Zellen hat.
5. Denke dir einen Namen für die Stelle aus, an der die Formen stehen.

## Unterstützung

- **Erlaubt:** Copilot erklärt Wörterbücher und verschachtelte Listen.
- **Verboten:** Keine fertigen Formen-Definitionen.

## Prüfen

**Manuell:** Dein Wörterbuch enthält genau sieben Arten mit je vier Zellen.

## Erwartetes Ergebnis

Sieben Arten, jede mit vier Zellen, sauber als Daten beschrieben.

## Definition of Done

- [ ] `tetromino.py` existiert.
- [ ] Ein Wörterbuch enthält alle sieben Arten I, O, T, S, Z, J, L.
- [ ] Jede Form hat genau vier Zellen.
- [ ] Die Formen lassen sich im Terminal ausgeben und prüfen.

## Verständnisfrage

Warum ist es praktisch, Formen als Daten zu beschreiben statt jede
Form einzeln „hart" ins Programm zu zeichnen?

## Hinweisleiter

1. **Leitfrage:** Welche Python-Datenstruktur verbindet einen Namen
   mit einem Wert?
2. **Konzeptueller Hinweis:** Eine Zeichenkette aus „X" und „." ist
   eine einfache Beschreibung einer Form.
3. **Algorithmus in Worten:** Für jede Art eine Form festlegen, alle in
   einem Wörterbuch sammeln.
4. **Pseudocode:** Wörterbuch mit Schlüsseln „I" bis „L".
5. **Beispiel (max. 5 Zeilen):** kleines Wörterbuch mit zwei Einträgen.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L02-E02-aktiven-stein-erzeugen.prompt.md`.
