# L02 · E02 · Aktiven Stein erzeugen

- **Lektion:** 2
- **Übung:** 2 von 5
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 20 Minuten
- **Voraussetzungen:** Übung 1 bestanden
- **Lernziel:** Du erzeugst einen aktiven Spielstein mit Art, Farbe
  und Form.
- **Sichtbares Ergebnis:** Beim Start des Programms wird ein Stein
  erzeugt und seine Art im Terminal ausgegeben.
- **Betroffene Dateien:** `lernprojekt/tetromino.py`,
  `lernprojekt/main.py`, `lernprojekt/settings.py`
- **Wichtige Begriffe:** Klasse, Objekt, Attribut, `__init__`

## Aufgabe in kleinen Schritten

1. Schreibe eine Klasse, die einen Stein beschreibt (Art, Farbe, Form).
2. Der Konstruktor soll die Art entgegennehmen und Form und Farbe
   zuordnen.
3. Lege in `settings.py` für jede Art eine eigene Farbe fest.
4. Erzeuge beim Start des Programms einen aktiven Stein und gib seine
   Art im Terminal aus.
5. Prüfe: Verhalten sich alle sieben Arten korrekt?

## Unterstützung

- **Erlaubt:** Copilot erklärt Klassen und Konstruktoren.
- **Verboten:** Keine fertige Klasse zum Abtippen.

## Prüfen

**Manuell:** Starte das Programm mehrmals — die ausgegebene Art
funktioniert jedes Mal fehlerfrei.

## Erwartetes Ergebnis

Eine Klasse, die aus einer Art einen Stein mit Farbe und Form macht.

## Definition of Done

- [ ] Eine Stein-Klasse mit Konstruktor existiert.
- [ ] Jede Art hat eine eigene Farbe.
- [ ] Beim Programmstart wird ein aktiver Stein erzeugt.
- [ ] Die Art des Steins wird ausgegeben und ist korrekt.

## Verständnisfrage

Was ist der Unterschied zwischen einer Klasse und einem Objekt?

## Hinweisleiter

1. **Leitfrage:** Wie heißt die Methode, die beim Erzeugen eines
   Objekts automatisch läuft?
2. **Konzeptueller Hinweis:** Eine Klasse bündelt Daten (Art, Farbe,
   Form) und Verhalten.
3. **Algorithmus in Worten:** Klasse schreiben, Art im Konstruktor
   speichern, Form und Farbe nachschlagen.
4. **Pseudocode:** Klasse mit Konstruktor und zwei Attributen.
5. **Beispiel (max. 5 Zeilen):** eine Mini-Klasse mit einem Attribut.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L02-E03-stein-zeichnen.prompt.md`.
