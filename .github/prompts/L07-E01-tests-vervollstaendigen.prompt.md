# L07 · E01 · Tests vervollständigen

- **Lektion:** 7
- **Übung:** 1 von 4
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 30 Minuten
- **Voraussetzungen:** Lektion 6 bestanden
- **Lernziel:** Du prüfst deine wichtigsten Spielfunktionen mit eigenen
  automatischen Tests.
- **Sichtbares Ergebnis:** Deine Testsuite deckt Spiellogik aus allen
  Lektionen ab und läuft vollständig grün.
- **Betroffene Dateien:** `lernprojekt/tests/`
- **Wichtige Begriffe:** Testabdeckung, Randfälle, Testname

## Aufgabe in kleinen Schritten

1. Sammle: Welche Funktionen deiner Spiellogik sind besonders wichtig?
2. Prüfe je Funktion mindestens den Normalfall und einen Randfall.
3. Nimm dir besonders vor: Grenzen, belegte Zellen, Reihen entfernen,
  Punkte, Level, Pause und Neustart.
4. Achte auf sprechende Testnamen („test_..." mit klarer Bedeutung).
5. Führe alle Tests aus und behebe echte Fehler in deinem Spielcode.

## Unterstützung

- **Erlaubt:** Copilot beschreibt Testfälle in Worten und nennt
  Eingaben und erwartete Ergebnisse.
- **Verboten:** Kein Testcode — du schreibst jeden Test selbst.

## Prüfen

**Automatisch:** `python -m unittest discover -s tests` (in `lernprojekt/`).

## Erwartetes Ergebnis

Eine aussagekräftige, vollständig grüne Testsuite.

## Definition of Done

- [ ] Mindestens ein Test pro Lektionsthema ab Lektion 3.
- [ ] Normalfälle und Randfälle sind abgedeckt.
- [ ] Alle Tests laufen erfolgreich.
- [ ] Die Testnamen erklären, was geprüft wird.

## Verständnisfrage

Warum testet man auch Randfälle — und nicht nur den „glücklichen" Weg?

## Hinweisleiter

1. **Leitfrage:** Was könnte bei dieser Funktion schiefgehen?
2. **Konzeptueller Hinweis:** Gute Tests beschreiben zuerst die
  Erwartung, dann die Handlung.
3. **Algorithmus in Worten:** Thema wählen, Fälle sammeln, Tests
  schreiben, ausführen, Fehler beheben.
4. **Pseudocode:** je Fall: vorbereiten, ausführen, vergleichen.
5. **Beispiel (max. 5 Zeilen):** ein Mini-Testmuster.

## Für Copilot

Beschreibe Testfälle nur in Worten; keine Testcode-Lieferung. Prüfe
Ergebnisse und erkläre Fehlschläge. Keine Datei verändern. Sprich die
Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L07-E02-code-aufraeumen.prompt.md`.
