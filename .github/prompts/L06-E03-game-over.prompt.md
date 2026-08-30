# L06 · E03 · Game Over

- **Lektion:** 6
- **Übung:** 3 von 5
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 25 Minuten
- **Voraussetzungen:** Übung 2 bestanden
- **Lernziel:** Dein Spiel erkennt, wenn kein neuer Stein mehr Platz hat
  — und zeigt „GAME OVER".
- **Sichtbares Ergebnis:** Ist die Startzone blockiert, endet das Spiel
  mit einer deutlichen Anzeige.
- **Betroffene Dateien:** `lernprojekt/game.py`, `lernprojekt/main.py`
- **Wichtige Begriffe:** Game Over, Startzone, blockiert

## Aufgabe in kleinen Schritten

1. Prüfe beim Erzeugen eines neuen Steins: Passt er überhaupt an
  seine Startposition?
2. Passt er nicht, setze den Zustand „Game Over".
3. Während Game Over: keine Schwerkraft, keine Eingaben für den Stein.
4. Zeige „GAME OVER" deutlich auf dem Bildschirm.
5. Teste absichtlich: Stapel so hoch, bis ein neuer Stein blockiert ist.

## Unterstützung

- **Erlaubt:** Copilot erklärt, warum die Startzone der beste Ort für
  die Game-Over-Prüfung ist.
- **Verboten:** Keine fertige Game-Over-Logik.

## Prüfen

**Manuell:** Bei blockierter Startzone erscheint „GAME OVER", das Feld
friert ein, und das Programm bleibt stabil.

## Erwartetes Ergebnis

Game Over wird zuverlässig erkannt und deutlich angezeigt.

## Definition of Done

- [ ] Beim Erzeugen eines Steins wird geprüft, ob er Platz hat.
- [ ] Ein eigener Game-Over-Zustand existiert.
- [ ] Bei Game Over reagiert der Stein nicht mehr.
- [ ] „GAME OVER" wird angezeigt.
- [ ] Das Programm stürzt dabei nicht ab.

## Verständnisfrage

Warum prüfst du Game Over genau beim Erzeugen eines neuen Steins?

## Hinweisleiter

1. **Leitfrage:** Was unterscheidet einen blockierten Start von einem
  normalen neuen Stein?
2. **Konzeptueller Hinweis:** „Neuer Stein" = Form an Startposition;
  ist dort keine Zelle frei, ist das Spiel vorbei.
3. **Algorithmus in Worten:** Stein erzeugen; passt er nicht, Zustand
  auf Game Over setzen und alles Weitere anhalten.
4. **Pseudocode:** wenn nicht platzierbar: game_over = True.
5. **Beispiel (max. 5 Zeilen):** Zuweisung eines Zustands nach einer Prüfung.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L06-E04-neustart.prompt.md`.
