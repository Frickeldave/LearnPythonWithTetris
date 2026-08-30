# L01 · E02 · Projekt anlegen

- **Lektion:** 1
- **Übung:** 2 von 5
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 15 Minuten
- **Voraussetzungen:** Übung 1 bestanden
- **Lernziel:** Du legst die ersten beiden Dateien deines Projekts an
  und weißt, wofür sie da sind.
- **Sichtbares Ergebnis:** Die Dateien `main.py` und `settings.py`
  existieren in `lernprojekt/` und lassen sich fehlerfrei starten.
- **Betroffene Dateien:** `lernprojekt/main.py`, `lernprojekt/settings.py`
- **Wichtige Begriffe:** Modul, Einstiegspunkt, Konstante

## Aufgabe in kleinen Schritten

1. Lege in `lernprojekt/` die Datei `main.py` an. Sie ist der
   Einstiegspunkt deines Spiels.
2. Gib der Datei eine kurze Beschreibung (Dokumentationskommentar).
3. Lege in `lernprojekt/` die Datei `settings.py` an. Dort sammelst du
   später Zahlen und Farben.
4. Lass `main.py` einmal laufen: Es darf noch nichts passieren, aber
   es darf auch keine Fehlermeldung geben.
5. Überlege: Warum legt man Einstellungen in eine eigene Datei?

## Unterstützung

- **Erlaubt:** Copilot erklärt, was ein Einstiegspunkt ist.
- **Verboten:** Kein fertiger Dateiinhalt.

## Prüfen

**Manuell:** `python main.py` läuft ohne Fehler durch und beendet sich.

## Erwartetes Ergebnis

Zwei Dateien sind vorhanden; `main.py` startet fehlerfrei.

## Definition of Done

- [ ] `main.py` existiert und enthält einen Beschreibungskommentar.
- [ ] `settings.py` existiert.
- [ ] `python main.py` läuft ohne Fehler.

## Verständnisfrage

Was ist der Unterschied zwischen einer Datei, die man direkt startet,
und einem Modul, das man importiert?

## Hinweisleiter

1. **Leitfrage:** Welche Datei startet Python, wenn du `python main.py`
   eingibst?
2. **Konzeptueller Hinweis:** Ein Modul ist einfach eine Python-Datei,
   die man importieren kann.
3. **Algorithmus in Worten:** Dateien anlegen, Kommentar schreiben,
   Start testen.
4. **Pseudocode:** nicht nötig — hier geht es nur um Dateien und einen Kommentar.
5. **Beispiel (max. 5 Zeilen):** wie ein Dokumentationskommentar aussieht.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L01-E03-fenster-oeffnen.prompt.md`.
