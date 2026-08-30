# L01 · E04 · Event-Loop

- **Lektion:** 1
- **Übung:** 4 von 5
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 20 Minuten
- **Voraussetzungen:** Übung 3 bestanden
- **Lernziel:** Du verstehst die Hauptschleife deines Spiels und
  verarbeitest Ereignisse (Events) wie Tastendruck und Schließen.
- **Sichtbares Ergebnis:** Das Fenster bleibt geöffnet, bis du es
  schließt oder Escape drückst.
- **Betroffene Dateien:** `lernprojekt/main.py`
- **Wichtige Begriffe:** Hauptschleife, Event, `pygame.event.get`,
  `pygame.QUIT`, `pygame.KEYDOWN`

## Aufgabe in kleinen Schritten

1. Ersetze den „einmaligen" Ablauf durch eine Schleife, die läuft,
   solange das Spiel nicht beendet wird.
2. Hole in jedem Durchlauf alle Ereignisse ab.
3. Beende die Schleife, wenn das Fenster geschlossen wird
   (Ereignis `QUIT`).
4. Beende die Schleife zusätzlich, wenn die Taste Escape gedrückt wird.
5. Begrenze die Wiederholungen pro Sekunde — sonst läuft die Schleife
   zu schnell.

## Unterstützung

- **Erlaubt:** Copilot erklärt, was ein Event ist und was `pygame.event`
   zurückgibt.
- **Verboten:** Keine komplette Hauptschleife zum Abtippen.

## Prüfen

**Manuell:** Das Fenster bleibt offen. X und Escape beenden das Spiel
sauber. Drückst du andere Tasten, passiert noch nichts.

## Erwartetes Ergebnis

Eine laufende Hauptschleife mit sauberem Beenden über X und Escape.

## Definition of Done

- [ ] Eine Hauptschleife läuft, bis das Spiel beendet wird.
- [ ] `QUIT` (Fenster-X) beendet das Spiel.
- [ ] Escape beendet das Spiel.
- [ ] Die Schleife ist auf eine sinnvolle Bildwiederholrate begrenzt.

## Verständnisfrage

Warum darf man Events nicht „zwischendrin" abfragen, sondern muss sie
regelmäßig in der Schleife abholen?

## Hinweisleiter

1. **Leitfrage:** Womit kannst du prüfen, ob ein Fenster geschlossen wurde?
2. **Konzeptueller Hinweis:** pygame sammelt Ereignisse in einer
   Warteschlange, die du mit einer Funktion ausliest.
3. **Algorithmus in Worten:** Solange nicht beendet: Events abholen,
   prüfen, ob beendet werden soll, Tempo begrenzen.
4. **Pseudocode:** Schleife mit „solange läuft", darin Event-Schleife.
5. **Beispiel (max. 5 Zeilen):** allgemeine Python-Schleife mit Abbruchbedingung.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L01-E05-spielfeld-zeichnen.prompt.md`.
