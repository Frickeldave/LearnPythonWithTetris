# L05 · E01 · Reihen erkennen

- **Lektion:** 5
- **Übung:** 1 von 5
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 15 Minuten
- **Voraussetzungen:** Lektion 4 bestanden
- **Lernziel:** Dein Spielfeld erkennt vollständig gefüllte Reihen.
- **Sichtbares Ergebnis:** Ein Test füllt eine Reihe komplett und dein
  Code meldet sie als „voll".
- **Betroffene Dateien:** `lernprojekt/board.py`, `lernprojekt/tests/`
- **Wichtige Begriffe:** volle Reihe, Prüfung, Liste

## Aufgabe in kleinen Schritten

1. Überlege: Woran erkennst du, dass eine Reihe voll ist?
2. Schreibe eine Funktion, die alle vollen Reihen zurückgibt.
3. Teste sie mit einer gefüllten, einer leeren und einer fast vollen Reihe.
4. Denke daran: Eine Reihe ist voll, wenn **jede** ihrer Zellen belegt ist.

## Unterstützung

- **Erlaubt:** Copilot erklärt die `all`-Funktion und Listen.
- **Verboten:** Keine fertige Funktion.

## Prüfen

**Automatisch:** Dein neuer Test läuft grün:
`python -m unittest discover -s tests`

## Erwartetes Ergebnis

Die Funktion liefert genau die vollen Reihen.

## Definition of Done

- [ ] Eine Funktion erkennt volle Reihen.
- [ ] Sie gibt alle vollen Reihen zurück.
- [ ] Ein eigener Test prüft volle, leere und fast volle Reihen.
- [ ] Der Test läuft erfolgreich.

## Verständnisfrage

Was muss für eine „volle Reihe" für jede einzelne Zelle gelten?

## Hinweisleiter

1. **Leitfrage:** Wie prüfst du, ob alle Elemente einer Liste belegt sind?
2. **Konzeptueller Hinweis:** Eine Reihe ist eine Liste von Zellen;
  „voll" heißt: kein Element ist leer.
3. **Algorithmus in Worten:** für jede Reihe prüfen, ob alle Zellen
  belegt sind; die Nummern der vollen Reihen sammeln.
4. **Pseudocode:** Schleife über Reihen mit Bedingung.
5. **Beispiel (max. 5 Zeilen):** `all`-Prüfung über eine Liste.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L05-E02-reihen-entfernen.prompt.md`.
