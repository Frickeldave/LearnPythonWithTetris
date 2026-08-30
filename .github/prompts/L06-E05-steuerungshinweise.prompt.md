# L06 · E05 · Steuerungshinweise

- **Lektion:** 6
- **Übung:** 5 von 5
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 15 Minuten
- **Voraussetzungen:** Übung 4 bestanden
- **Lernziel:** Dein Spiel zeigt die Steuerung direkt im Fenster an.
- **Sichtbares Ergebnis:** Im Seitenbereich steht eine kompakte Liste
  aller Tasten und ihrer Wirkung.
- **Betroffene Dateien:** `lernprojekt/main.py`
- **Wichtige Begriffe:** Bedienungsanleitung, Textliste, Übersicht

## Aufgabe in kleinen Schritten

1. Sammle alle Tasten deines Spiels und ihre Wirkung.
2. Zeichne sie als kurze, gut lesbare Liste in den Seitenbereich.
3. Nutze eine Schleife über eine Liste statt vieler einzelner
  Textzeichnungen.
4. Prüfe: Jede Taste aus deiner Event-Verarbeitung taucht in der Liste auf.

## Unterstützung

- **Erlaubt:** Copilot hilft dir, deine Tastenliste zu vervollständigen.
- **Verboten:** Keine fertige Anzeige.

## Prüfen

**Manuell:** Die Liste ist lesbar und vollständig — auch für jemanden,
der das Spiel noch nie gespielt hat.

## Erwartetes Ergebnis

Eine vollständige, gut lesbare Steuerungsübersicht im Fenster.

## Definition of Done

- [ ] Alle Tasten sind in der Anzeige aufgeführt.
- [ ] Die Liste ist im Seitenbereich gut lesbar.
- [ ] Die Anzeige wird über eine Liste per Schleife gezeichnet.

## Verständnisfrage

Warum schreibt man Wiederholungen wie eine Textliste lieber als
Schleife statt als viele Einzelaufrufe?

## Hinweisleiter

1. **Leitfrage:** Welche Tasten behandelt dein Code aktuell?
2. **Konzeptueller Hinweis:** Eine Liste aus (Text-)Zeilen lässt sich
  mit einer Schleife zeilenweise anzeigen.
3. **Algorithmus in Worten:** Liste der Hinweise anlegen, für jede
  Zeile Text rendern und mit Abstand anzeigen.
4. **Pseudocode:** für zeile, position in Liste: anzeigen(zeile, y).
5. **Beispiel (max. 5 Zeilen):** Schleife, die Texte untereinander ausgibt.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Das Basisspiel ist fertig — herzlichen Glückwunsch!
Lektions-Gate mit `00-lektions-gate.prompt.md`, dann Lektion 7.
