# L02 · E03 · Stein zeichnen

- **Lektion:** 2
- **Übung:** 3 von 5
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 25 Minuten
- **Voraussetzungen:** Übung 2 bestanden
- **Lernziel:** Du zeichnest den aktiven Stein an seiner Position auf
  dem Spielfeld.
- **Sichtbares Ergebnis:** Der Stein erscheint oben in der Mitte des
  Spielfelds in seiner Art-Farbe.
- **Betroffene Dateien:** `lernprojekt/main.py`, `lernprojekt/tetromino.py`
- **Wichtige Begriffe:** Zelle, Position (x, y), Versatz, `pygame.Rect`

## Aufgabe in kleinen Schritten

1. Überlege: Wo in der Breite soll ein neuer Stein erscheinen?
2. Speichere die Position des aktiven Steins als x- und y-Wert.
3. Bestimme für die Form des Steins alle Zellen (Versatz zur Position).
4. Zeichne jede Zelle als gefülltes Rechteck in der Farbe des Steins.
5. Achte darauf, dass der Stein **vor** den Gitterlinien gezeichnet wird.

## Unterstützung

- **Erlaubt:** Copilot erklärt, wie man aus einer Form eine Zellliste macht.
- **Verboten:** Keine fertige Zeichenfunktion.

## Prüfen

**Manuell:** Beim Start ist ein Stein oben mittig sichtbar; seine Farbe
passt zu seiner Art.

## Erwartetes Ergebnis

Der aktive Stein wird an seiner Startposition korrekt gezeichnet.

## Definition of Done

- [ ] Die Position des Steins ist gespeichert.
- [ ] Alle Zellen des Steins werden aus der Form bestimmt.
- [ ] Der Stein wird an der richtigen Stelle gezeichnet.
- [ ] Der Stein ist über dem Gitter sichtbar, nicht dahinter versteckt.

## Verständnisfrage

Warum rechnet man die Zellen einer Form relativ zur Position des Steins
statt absolut?

## Hinweisleiter

1. **Leitfrage:** Wo in deinem Code liegt die Form des Steins?
2. **Konzeptueller Hinweis:** Position + Versatz = echte Bildschirmzelle.
3. **Algorithmus in Worten:** Für jede belegte Zelle der Form ein
   Rechteck an Position plus Versatz zeichnen.
4. **Pseudocode:** Schleife über die Zellen, darin ein Rechteck.
5. **Beispiel (max. 5 Zeilen):** Schleife, die zwei Rechtecke an
   berechneten Positionen zeichnet.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L02-E04-seven-bag.prompt.md`.
