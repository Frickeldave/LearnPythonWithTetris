# L06 · E04 · Neustart

- **Lektion:** 6
- **Übung:** 4 von 5
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 15 Minuten
- **Voraussetzungen:** Übung 3 bestanden
- **Lernziel:** Mit R startest du ein neues Spiel, ohne das Programm zu
  schließen.
- **Sichtbares Ergebnis:** R setzt Spielfeld, Punkte, Level und Steine
  in den Anfangszustand zurück.
- **Betroffene Dateien:** `lernprojekt/game.py`, `lernprojekt/main.py`
- **Wichtige Begriffe:** Zurücksetzen, Anfangszustand, Neuinitialisierung

## Aufgabe in kleinen Schritten

1. Überlege: Was gehört alles zum „Anfangszustand"?
2. Schreibe eine Funktion, die all diese Dinge zurücksetzt.
3. Nutze sie beim ersten Start **und** bei jedem R.
4. Prüfe, dass nach dem Neustart wirklich nichts Altes übrig bleibt.
5. Der Neustart soll auch mitten im Spiel und nach Game Over funktionieren.

## Unterstützung

- **Erlaubt:** Copilot erklärt, warum eine gemeinsame Reset-Funktion
  doppelte Logik vermeidet.
- **Verboten:** Keine fertige Reset-Funktion.

## Prüfen

**Manuell:** R während des Spiels und nach Game Over bringt ein frisches
Feld mit 0 Punkten, Level 1 und einem neuen Stein.

## Erwartetes Ergebnis

Neustart per R aus jedem Zustand heraus, ohne Programmneustart.

## Definition of Done

- [ ] Eine Reset-Funktion setzt alle Spielwerte zurück.
- [ ] R ruft die Reset-Funktion auf.
- [ ] Der Neustart funktioniert mitten im Spiel und nach Game Over.
- [ ] Der erste Start nutzt dieselbe Funktion.

## Verständnisfrage

Warum ist es gut, den ersten Start und den Neustart über dieselbe
Funktion laufen zu lassen?

## Hinweisleiter

1. **Leitfrage:** Welche Werte muss ein „frisches Spiel" haben?
2. **Konzeptueller Hinweis:** Alles, was du beim Start belegst, gehört
  in die Reset-Funktion — auch Pause und Game Over.
3. **Algorithmus in Worten:** Feld leeren, Zähler nullen, Zustände
  zurücksetzen, ersten Stein erzeugen.
4. **Pseudocode:** Funktion, die alle Anfangs-Zuweisungen bündelt.
5. **Beispiel (max. 5 Zeilen):** Funktion mit mehreren Zuweisungen.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L06-E05-steuerungshinweise.prompt.md`.
