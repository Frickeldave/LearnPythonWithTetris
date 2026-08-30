# L03 · E04 · Kollisionstests

- **Lektion:** 3
- **Übung:** 4 von 4
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 30 Minuten
- **Voraussetzungen:** Übung 3 bestanden
- **Lernziel:** Du schreibst deine ersten eigenen automatischen Tests
  für Grenzen und belegte Zellen.
- **Sichtbares Ergebnis:** `python -m unittest discover -s tests`
  meldet mehrere erfolgreiche Tests.
- **Betroffene Dateien:** `lernprojekt/tests/test_*.py`
- **Wichtige Begriffe:** `unittest`, Testfall, Arrange–Act–Assert,
  Erwartung

## Aufgabe in kleinen Schritten

1. Lege eine erste Testdatei unter `tests/` an.
2. Denke an Arrange–Act–Assert: erst alles vorbereiten, dann handeln,
   dann prüfen.
3. Teste mindestens: eine Zelle innerhalb des Felds, eine außerhalb,
   eine freie und eine belegte Zelle.
4. Teste, dass eine Bewegung an einer belegten Zelle abgelehnt wird.
5. Führe deine Tests aus und behebe Fehler — in deinem Code, nicht in
   den Erwartungen (außer die Erwartung war wirklich falsch).

## Unterstützung

- **Erlaubt:** Copilot beschreibt Testfälle in Worten, nennt Eingaben
  und erwartete Ergebnisse und erklärt `unittest`.
- **Verboten:** Kein vollständiger Testcode — die Tests schreibst du selbst.

## Prüfen

**Automatisch:** `python -m unittest discover -s tests` (in `lernprojekt/`).

## Erwartetes Ergebnis

Mindestens vier eigene Tests laufen grün.

## Definition of Done

- [ ] Eine Testdatei unter `tests/` existiert.
- [ ] Mindestens vier Tests prüfen Grenzen und belegte Zellen.
- [ ] Alle Tests laufen erfolgreich durch.
- [ ] Du kannst erklären, was jeder Test prüft.

## Verständnisfrage

Was bedeutet „Arrange, Act, Assert" — und warum ist die Reihenfolge wichtig?

## Hinweisleiter

1. **Leitfrage:** Was muss ein Test tun, damit `unittest` ihn erkennt?
2. **Konzeptueller Hinweis:** Ein Test ist eine Methode, die mit
   „test_" beginnt und mit Prüfmethoden (z. B. `assertTrue`) arbeitet.
3. **Algorithmus in Worten:** Objekt vorbereiten, Aktion ausführen,
   Ergebnis mit Erwartung vergleichen.
4. **Pseudocode:** Klasse mit Methoden, darin je eine Prüfung.
5. **Beispiel (max. 5 Zeilen):** Mini-Test mit einer Prüfung.

## Für Copilot

Beschreibe Testfälle nur in Worten; liefere keinen Testcode. Prüfe die
vorhandenen Tests und erkläre Ergebnisse. Keine Datei verändern.
Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Lektion 3 ist komplett: Lektions-Gate mit `00-lektions-gate.prompt.md`.
