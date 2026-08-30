# L01 · E05 · Spielfeld zeichnen

- **Lektion:** 1
- **Übung:** 5 von 5
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 25 Minuten
- **Voraussetzungen:** Übung 4 bestanden
- **Lernziel:** Du zeichnest das Spielfeld: 10 Spalten, 20 sichtbare
  Reihen, Raster und Hintergrund.
- **Sichtbares Ergebnis:** Das Fenster zeigt das 10 × 20-Spielfeld mit
  Gitternetz.
- **Betroffene Dateien:** `lernprojekt/main.py`, `lernprojekt/settings.py`
- **Wichtige Begriffe:** Raster, Zelle, Pixel, `pygame.draw`, `flip`

## Aufgabe in kleinen Schritten

1. Lege in `settings.py` fest: 10 Spalten, 20 Reihen, Zellengröße in
   Pixeln und Farben (Hintergrund, Gitterlinien).
2. Berechne die Fenstergröße aus Spalten, Reihen und Zellengröße —
   nicht als „fertig ausgerechnete" Zahl.
3. Fülle in `main.py` jeden Durchlauf zuerst den Hintergrund.
4. Zeichne senkrechte und waagerechte Linien für das Gitternetz.
5. Sorge dafür, dass das Gezeichnete wirklich sichtbar wird.

## Unterstützung

- **Erlaubt:** Copilot erklärt Schleifen zum Zeichnen vieler Linien.
- **Verboten:** Keine fertige Zeichenfunktion.

## Prüfen

**Manuell:** Ein sauberes 10 × 20-Raster ist sichtbar, das Fenster hat
die richtige Größe.

## Erwartetes Ergebnis

10 Spalten und 20 Reihen als Gitternetz, Größe aus Konstanten berechnet.

## Definition of Done

- [ ] `settings.py` enthält Spalten, Reihen, Zellengröße und Farben.
- [ ] Die Fenstergröße wird aus diesen Konstanten berechnet.
- [ ] Hintergrund und Gitternetz werden jede Runde gezeichnet.
- [ ] Das Ergebnis wird sichtbar gemacht (Fenster aktualisiert).

## Verständnisfrage

Warum berechnest du die Fenstergröße aus Konstanten, statt sie einfach
als Zahl hinzuschreiben?

## Hinweisleiter

1. **Leitfrage:** Wie viele Pixel breit ist eine Zeile mit 10 Zellen
   bei 30 Pixeln pro Zelle?
2. **Konzeptueller Hinweis:** Eine Linie hat Start- und Endpunkt in
   Pixeln; Pixel = Zelle × Zellengröße.
3. **Algorithmus in Worten:** Für jede Spaltengrenze eine senkrechte
   Linie, für jede Reihengrenze eine waagerechte.
4. **Pseudocode:** zwei `for`-Schleifen über Spalten und Reihen.
5. **Beispiel (max. 5 Zeilen):** einfache `for`-Schleife, die
   nacheinander Linien zeichnet.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Damit ist Lektion 1 komplett: Lektions-Gate mit `00-lektions-gate.prompt.md`.
