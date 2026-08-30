# L03 · E03 · Belegte Zellen

- **Lektion:** 3
- **Übung:** 3 von 4
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 20 Minuten
- **Voraussetzungen:** Übung 2 bestanden
- **Lernziel:** Dein Spielfeld kennt belegte Zellen; der Stein stoppt
  auch an bereits gelandeten Blöcken.
- **Sichtbares Ergebnis:** Ein Test belegt Zellen im Feld, und der
  Stein kann diese Zellen nicht überqueren oder betreten.
- **Betroffene Dateien:** `lernprojekt/board.py` (oder ähnlich),
  `lernprojekt/main.py`
- **Wichtige Begriffe:** Raster, belegte Zelle, Gitter, Zustand

## Aufgabe in kleinen Schritten

1. Lege eine Datenstruktur für das Spielfeld an: 10 × 20 Zellen,
   anfangs alle frei.
2. Schreibe eine Prüfung: Ist eine bestimmte Zelle frei?
3. Behandle den Bereich über dem Feld als frei (dort fallen Steine herein).
4. Prüfe in deiner Bewegung zusätzlich: Sind alle Zielzellen frei?
5. Zeichne belegte Zellen in ihrer gespeicherten Farbe.

## Unterstützung

- **Erlaubt:** Copilot erklärt Listen von Listen (Gitter) und warum
  die oberste Reihe Index 0 hat.
- **Verboten:** Keine fertige Board-Klasse.

## Prüfen

**Manuell:** Mit einem kleinen Test (ein paar manuell belegte Zellen)
  bleibt der Stein vor belegten Zellen stehen.

## Erwartetes Ergebnis

Bewegung berücksichtigt belegte Zellen; diese werden farbig gezeichnet.

## Definition of Done

- [ ] Das Spielfeld speichert 10 × 20 Zellen.
- [ ] Eine Prüfung „Zelle frei?" existiert.
- [ ] Über dem Feld gilt alles als frei.
- [ ] Die Bewegung prüft alle Zielzellen.
- [ ] Belegte Zellen werden farbig gezeichnet.

## Verständnisfrage

Warum ist das Spielfeld ein eigener Zustand, getrennt vom aktiven Stein?

## Hinweisleiter

1. **Leitfrage:** Wie speicherst du ein Gitter aus Reihen und Spalten?
2. **Konzeptueller Hinweis:** Eine leere Zelle ist `None`; eine belegte
   Zelle speichert eine Farbe.
3. **Algorithmus in Worten:** Gitter anlegen, Zelle prüfen, bei
   Bewegung alle Zielzellen prüfen, belegte Zellen zeichnen.
4. **Pseudocode:** zweidimensionale Liste mit `None`.
5. **Beispiel (max. 5 Zeilen):** kleine 2×2-Liste mit einem Eintrag.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L03-E04-kollisionstests.prompt.md`.
