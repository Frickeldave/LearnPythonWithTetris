# L06 · E01 · Statusanzeige

- **Lektion:** 6
- **Übung:** 1 von 5
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 20 Minuten
- **Voraussetzungen:** Lektion 5 bestanden
- **Lernziel:** Dein Spiel zeigt Punkte, Level und entfernte Reihen an.
- **Sichtbares Ergebnis:** In einem Seitenbereich stehen dauerhaft
  „Punkte", „Level" und „Reihen" mit aktuellen Werten.
- **Betroffene Dateien:** `lernprojekt/main.py`
- **Wichtige Begriffe:** Textdarstellung, Schrift, `render`, `blit`

## Aufgabe in kleinen Schritten

1. Verbreitere dein Fenster um einen Seitenbereich (falls nicht schon
  aus Lektion 2 vorhanden).
2. Zeichne dort drei Zeilen Text: Punkte, Level, Reihen.
3. Aktualisiere die Texte in jedem Durchlauf mit den echten Werten.
4. Prüfe: Die Zahlen stimmen immer mit dem Spielgeschehen überein.

## Unterstützung

- **Erlaubt:** Copilot erklärt, wie Text in pygame auf den Bildschirm kommt.
- **Verboten:** Keine fertige Anzeige-Funktion.

## Prüfen

**Manuell:** Nach einem Hard Drop und nach einer entfernten Reihe
ändern sich die Zahlen sofort korrekt.

## Erwartetes Ergebnis

Live-Anzeige von Punkten, Level und Reihen im Seitenbereich.

## Definition of Done

- [ ] Ein Seitenbereich existiert.
- [ ] Punkte, Level und Reihen werden als Text angezeigt.
- [ ] Die Werte werden laufend aktualisiert.
- [ ] Die Anzeige bleibt auch bei langem Spiel lesbar.

## Verständnisfrage

Warum zeichnet man Text jeden Durchlauf neu, statt ihn nur einmal zu setzen?

## Hinweisleiter

1. **Leitfrage:** Woraus entsteht ein sichtbarer Text in pygame?
2. **Konzeptueller Hinweis:** Erst wird der Text als Bild „gerendert",
  dann an eine Position „geblittet".
3. **Algorithmus in Worten:** Text mit Wert bauen, rendern, im
  Seitenbereich anzeigen — jedes Bild neu.
4. **Pseudocode:** für jede Zeile: bild = schrift.render(text); blit.
5. **Beispiel (max. 5 Zeilen):** einen Text rendern und anzeigen.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L06-E02-pause.prompt.md`.
