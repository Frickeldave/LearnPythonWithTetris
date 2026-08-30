# L04 · E03 · Rotation

- **Lektion:** 4
- **Übung:** 3 von 4
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 30 Minuten
- **Voraussetzungen:** Übung 2 bestanden
- **Lernziel:** Du drehst den aktiven Stein in beide Richtungen.
- **Sichtbares Ergebnis:** Pfeil hoch oder X dreht im Uhrzeigersinn,
  Z dreht gegen den Uhrzeigersinn.
- **Betroffene Dateien:** `lernprojekt/tetromino.py`,
  `lernprojekt/main.py`
- **Wichtige Begriffe:** Rotation, Matrix, 90 Grad, Koordinaten

## Aufgabe in kleinen Schritten

1. Überlege zuerst auf Papier: Wohin wandert eine Zelle (x, y) bei
  einer 90-Grad-Drehung?
2. Schreibe eine Drehung für deine Formbeschreibung — in beide Richtungen.
3. Binde die Drehung an zwei Tasten (im und gegen den Uhrzeigersinn).
4. Prüfe vor der Drehung wie bei der Bewegung: Passt der gedrehte
  Stein an seine Position?
5. Behandle den O-Stein: Drehen darf ihn nicht verändern (er sieht ja
  gleich aus).

## Unterstützung

- **Erlaubt:** Copilot erklärt Matrizen-Drehung und Koordinatenformeln.
- **Verboten:** Keine fertige Dreh-Funktion.

## Prüfen

**Manuell:** Jeder Stein dreht sich mit den Tasten in beide Richtungen
und bleibt dabei innerhalb des Felds.

## Erwartetes Ergebnis

Rotation in beide Richtungen für alle Arten, mit Kollisionsprüfung.

## Definition of Done

- [ ] Es gibt eine Drehung im und eine gegen den Uhrzeigersinn.
- [ ] Beide sind an Tasten gebunden.
- [ ] Die gedrehte Form wird nur übernommen, wenn sie passt.
- [ ] Der O-Stein bleibt beim Drehen unverändert.

## Verständnisfrage

Warum darfst du die Form nicht einfach „vorab" ändern, ohne zu prüfen?

## Hinweisleiter

1. **Leitfrage:** Wie beschreibst du die Drehung einer einzelnen Zelle
  um den Mittelpunkt?
2. **Konzeptueller Hinweis:** Drehen = Form ausprobieren, prüfen, bei
  Erfolg übernehmen, sonst zurücknehmen.
3. **Algorithmus in Worten:** Form gedanklich drehen, alle Zellen
  prüfen, nur bei Erfolg tatsächlich übernehmen.
4. **Pseudocode:** kopiere Form, drehe Kopie, prüfe, dann ersetzen.
5. **Beispiel (max. 5 Zeilen):** Vertauschen von x und y in einer Schleife.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L04-E04-wall-kick.prompt.md`.
