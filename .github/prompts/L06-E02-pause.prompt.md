# L06 · E02 · Pause

- **Lektion:** 6
- **Übung:** 2 von 5
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 15 Minuten
- **Voraussetzungen:** Übung 1 bestanden
- **Lernziel:** Mit P pausierst und setzt du das Spiel fort.
- **Sichtbares Ergebnis:** Während der Pause fällt nichts, der Stein
  reagiert nicht, und „PAUSE" steht auf dem Bildschirm.
- **Betroffene Dateien:** `lernprojekt/game.py`, `lernprojekt/main.py`
- **Wichtige Begriffe:** Zustand, Pause, Umschalten

## Aufgabe in kleinen Schritten

1. Führe einen Pause-Zustand ein (ein Wahrheitswert).
2. P schaltet den Zustand um.
3. Während der Pause: keine Schwerkraft, keine Bewegung, keine Drehung.
4. Zeige „PAUSE" deutlich auf dem Bildschirm.
5. Beende die Pause mit einem erneuten Druck auf P.

## Unterstützung

- **Erlaubt:** Copilot erklärt das Umschalten eines Zustands.
- **Verboten:** Keine fertige Pause-Logik.

## Prüfen

**Manuell:** P friert das Spiel vollständig ein, ein zweites P spielt
weiter — nichts „holt nach" (kein Steinhagel nach der Pause).

## Erwartetes Ergebnis

Saubere Pause mit sichtbarer Anzeige und ohne Nachhol-Effekte.

## Definition of Done

- [ ] Ein Pause-Zustand existiert.
- [ ] P schaltet Pause an und aus.
- [ ] In der Pause reagiert nichts im Spiel.
- [ ] „PAUSE" wird angezeigt.
- [ ] Nach der Pause läuft das Spiel normal weiter.

## Verständnisfrage

Warum darf die Schwerkraft-Zeit während der Pause nicht weiterlaufen?

## Hinweisleiter

1. **Leitfrage:** Wo in deinem Ablauf entscheidest du, ob das Spiel
  gerade „tickt"?
2. **Konzeptueller Hinweis:** Ein Zustand wie `pausiert` wird in allen
  Aktionen (fallen, bewegen, drehen) abgefragt.
3. **Algorithmus in Worten:** Zustand umschalten; jede Aktion beginnt
  mit „wenn nicht pausiert".
4. **Pseudocode:** wenn pausiert: nichts tun; sonst normal ablaufen.
5. **Beispiel (max. 5 Zeilen):** `if`-Abfrage vor einer Aktion.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L06-E03-game-over.prompt.md`.
