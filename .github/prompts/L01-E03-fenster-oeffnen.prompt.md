# L01 · E03 · Fenster öffnen

- **Lektion:** 1
- **Übung:** 3 von 5
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 20 Minuten
- **Voraussetzungen:** Übung 2 bestanden
- **Lernziel:** Du öffnest mit pygame ein Spielfenster mit Titel und
  schließt es sauber wieder.
- **Sichtbares Ergebnis:** Ein Fenster mit dem Titel „Blockfall" öffnet
  sich und lässt sich über das X schließen.
- **Betroffene Dateien:** `lernprojekt/main.py`, `lernprojekt/settings.py`
- **Wichtige Begriffe:** `pygame.init`, `set_mode`, `set_caption`,
  `pygame.quit`, Pixel

## Aufgabe in kleinen Schritten

1. Importiere pygame in `main.py` und initialisiere es.
2. Öffne ein Fenster. Überlege dir Breite und Höhe in Pixeln.
3. Gib dem Fenster den Titel „Blockfall".
4. Sorge dafür, dass sich das Fenster über das X schließen lässt.
5. Lege eine Fenstergröße als Konstante in `settings.py` ab und
   benutze sie in `main.py`.

## Unterstützung

- **Erlaubt:** Copilot erklärt die pygame-Funktionen einzeln.
- **Verboten:** Keine komplette `main.py`.

## Prüfen

**Manuell:** Das Fenster öffnet sich mit dem richtigen Titel und
schließt über das X, ohne dass das Terminal hängen bleibt.

## Erwartetes Ergebnis

Fenster sichtbar, Titel korrekt, sauberes Schließen.

## Definition of Done

- [ ] `main.py` importiert und initialisiert pygame.
- [ ] Ein Fenster mit dem Titel „Blockfall" öffnet sich.
- [ ] Das X schließt das Fenster und beendet das Programm sauber.
- [ ] Die Fenstergröße steht in `settings.py`.

## Verständnisfrage

Was bedeutet `pygame.init()` — und warum rufst du es vor dem Öffnen
eines Fensters auf?

## Hinweisleiter

1. **Leitfrage:** Welche Funktion erzeugt das eigentliche Fenster?
2. **Konzeptueller Hinweis:** pygame muss zuerst gestartet werden,
   bevor du ein Fenster anlegen kannst.
3. **Algorithmus in Worten:** initialisieren, Fenster anlegen, Titel
   setzen, auf das Schließen reagieren, pygame beenden.
4. **Pseudocode:** kurze Abfolge der genannten Schritte.
5. **Beispiel (max. 5 Zeilen):** nur das Grundmuster, kein fertiges Spiel.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L01-E04-event-loop.prompt.md`.
