# L07 · E02 · Code aufräumen

- **Lektion:** 7
- **Übung:** 2 von 4
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 25 Minuten
- **Voraussetzungen:** Übung 1 bestanden
- **Lernziel:** Du verbesserst Verständlichkeit und Ordnung deines Codes,
  ohne sein Verhalten zu verändern.
- **Sichtbares Ergebnis:** Nach dem Aufräumen laufen Spiel und Tests
  unverändert fehlerfrei — der Code ist aber deutlich lesbarer.
- **Betroffene Dateien:** alle Dateien in `lernprojekt/`
- **Wichtige Begriffe:** Refactoring, sprechende Namen, magische Zahlen

## Aufgabe in kleinen Schritten

1. Mache zuerst ein Code-Review (Prompt `00-code-review.prompt.md`).
2. Verbessere sprechende Namen: Was tut diese Variable wirklich?
3. Ersetze „magische Zahlen" durch Konstanten in `settings.py`.
4. Teile zu lange Funktionen in kleinere mit klarer Aufgabe.
5. Prüfe nach **jeder** Änderung: Tests und Spiel laufen noch.

## Unterstützung

- **Erlaubt:** Copilot nennt Verbesserungsideen und prüft deinen Code —
  geändert wird nur von dir.
- **Verboten:** Keine „fertig aufgeräumte" Datei.

## Prüfen

**Automatisch:** `python -m unittest discover -s tests` und
`python tools/check_lesson.py --lesson all` (vom Wurzelverzeichnis).

## Erwartetes Ergebnis

Lesbarer Code bei unverändertem Verhalten.

## Definition of Done

- [ ] Verbesserungen aus dem Review sind umgesetzt (oder bewusst verworfen).
- [ ] Es gibt keine unerklärten Zahlen mehr im Code.
- [ ] Funktionen sind kurz und haben je eine Aufgabe.
- [ ] Tests und Kursprüfungen laufen weiter grün.

## Verständnisfrage

Woran merkst du, dass ein Refactoring erfolgreich war?

## Hinweisleiter

1. **Leitfrage:** Versteht ein Außenstehender diese Zeile auf Anhieb?
2. **Konzeptueller Hinweis:** Refactoring ändert die Form, nicht das
  Verhalten — Tests schützen dich dabei.
3. **Algorithmus in Worten:** Stelle verbessern, Tests laufen lassen,
  erst dann die nächste Stelle.
4. **Pseudocode:** nicht nötig — hier geht es ums Lesen und Ordnen.
5. **Beispiel (max. 5 Zeilen):** Namensverbesserung vorher/nachher.

## Für Copilot

Gib nur Rückmeldung und Hinweise; keine Änderungen, keine Lösungen.
Nach jeder Änderung erneut prüfen. Sprich die Person mit ihrem Namen
an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L07-E03-readme-schreiben.prompt.md`.
