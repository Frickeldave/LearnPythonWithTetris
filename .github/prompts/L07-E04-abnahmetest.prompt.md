# L07 · E04 · Abnahmetest

- **Lektion:** 7
- **Übung:** 4 von 4
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 20 Minuten
- **Voraussetzungen:** Übungen 1–3 bestanden
- **Lernziel:** Du prüfst dein fertiges Spiel einmal komplett — mit
  allen automatischen und manuellen Prüfungen.
- **Sichtbares Ergebnis:** Alle Prüfungen sind grün, und die
  Abschlussprüfung ist bestanden.
- **Betroffene Dateien:** alle in `lernprojekt/`
- **Wichtige Begriffe:** Abnahme, vollständige Prüfung, Definition of Done

## Aufgabe in kleinen Schritten

1. Führe deine eigenen Tests aus: `python -m unittest discover -s tests`.
2. Führe die vollständige Kursprüfung aus:
   `python tools/check_lesson.py --lesson all` (vom Wurzelverzeichnis).
3. Gehe die Liste der Pflichtfunktionen in `docs/ABNAHMETEST.md` durch
   und prüfe jede am laufenden Spiel.
4. Starte die Abschlussprüfung mit `00-abschlusspruefung.prompt.md`
   und beantworte die Verständnisfragen.
5. Trage dein Ergebnis in `PROGRESS.md` ein (ohne persönliche Daten).

## Unterstützung

- **Erlaubt:** Copilot führt Prüfungen aus, erklärt Ergebnisse und
  hilft bei Nacharbeit mit der Hinweisleiter.
- **Verboten:** Keine Dateiänderungen, keine Lösungen, keine
  Bonusaufgabe als Pflicht.

## Prüfen

**Automatisch:** beide Testläufe oben.
**Manuell:** alle Punkte aus `docs/ABNAHMETEST.md`.

## Erwartetes Ergebnis

Basisabnahme: BESTANDEN.

## Definition of Done

- [ ] Eigene Tests laufen grün.
- [ ] `check_lesson.py --lesson all` meldet für alle Lektionen BESTANDEN.
- [ ] Alle manuellen Prüfungen sind bestätigt.
- [ ] Die Verständnisfragen sind beantwortet.
- [ ] `PROGRESS.md` ist aktuell.

## Verständnisfrage

Warum reicht „Tests sind grün" allein nicht für eine vollständige Abnahme?

## Hinweisleiter

1. **Leitfrage:** Welche Prüfungen kann ein Computer nicht für dich machen?
2. **Konzeptueller Hinweis:** Automatische Tests prüfen Logik; Gefühl,
  Bedienbarkeit und Vollständigkeit prüfst du am laufenden Spiel.
3. **Algorithmus in Worten:** automatisch prüfen, manuell prüfen,
  dokumentieren, Abschlussprüfung starten.
4. **Pseudocode:** nicht nötig.
5. **Beispiel (max. 5 Zeilen):** eine Abhakliste.

## Für Copilot

Führe die Prüfungen aus und erläutere sie; bei Nacharbeit Hinweisleiter.
Keine Datei verändern. Sprich die Person mit ihrem Namen an.

## Abschluss

Bei BESTANDEN: herzlichen Glückwunsch zum fertigen Blockfall!
Weiter geht es freiwillig mit `L07-B01-eigene-erweiterung.prompt.md`.
