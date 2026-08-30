# L04 · E04 · Wall Kick

- **Lektion:** 4
- **Übung:** 4 von 4
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 20 Minuten
- **Voraussetzungen:** Übung 3 bestanden
- **Lernziel:** Passt ein gedrehter Stein nicht an seiner Position,
  probiert dein Spiel ein paar kleine Ausweichpositionen (Wall Kick).
- **Sichtbares Ergebnis:** Drehen an der Wand schiebt den Stein sanft
  zurück ins Feld, statt die Drehung einfach abzulehnen.
- **Betroffene Dateien:** `lernprojekt/main.py` (oder deine Logik-Datei)
- **Wichtige Begriffe:** Wall Kick, Versatz, Ausweichposition

## Aufgabe in kleinen Schritten

1. Prüfe nach einer Drehung zuerst die aktuelle Position.
2. Passt sie nicht, probiere nacheinander: ein Feld nach links,
  ein Feld nach rechts, ein Feld nach oben.
3. Die erste passende Position wird übernommen.
4. Passt keine Position, nimm die Drehung zurück.
5. Dokumentiere in einer Kommentarzeile, dass dies ein **vereinfachtes**
  Wall-Kick-System ist (bewusst einfacher als offizielles Tetris).

## Unterstützung

- **Erlaubt:** Copilot erklärt, warum Reihenfolge und Grenzen der
  Ausweichpositionen wichtig sind.
- **Verboten:** Keine fertige Kick-Funktion.

## Prüfen

**Manuell:** Drehe einen Stein direkt an der linken und an der rechten
Wand — er bleibt im Feld, ohne „durch die Wand" zu gehen.

## Erwartetes Ergebnis

Drehungen an Wänden funktionieren dank Wall Kick; unmögliche Drehungen
werden sauber zurückgenommen.

## Definition of Done

- [ ] Nach der Drehung wird die aktuelle Position geprüft.
- [ ] Ausweichpositionen: links, rechts, oben (jeweils ein Feld).
- [ ] Die erste passende Position wird übernommen.
- [ ] Passt keine, wird die Drehung zurückgenommen.
- [ ] Ein Kommentar dokumentiert das vereinfachte Wall-Kick-System.

## Verständnisfrage

Warum probiert man die Positionen in einer festen Reihenfolge statt
„irgendeine passende" zu suchen?

## Hinweisleiter

1. **Leitfrage:** Was ist der Unterschied zwischen „Drehung ablehnen"
  und „Drehung woandershin verschieben"?
2. **Konzeptueller Hinweis:** Eine kleine Liste von Versatzpaaren
  (dx, dy) lässt sich der Reihe nach durchprobieren.
3. **Algorithmus in Worten:** für jede Position in fester Reihenfolge:
  prüfen; erste passende nehmen; sonst Drehung zurücknehmen.
4. **Pseudocode:** für (dx, dy) in Liste: wenn passt → übernehmen und fertig.
5. **Beispiel (max. 5 Zeilen):** Schleife über eine kleine Liste von Paaren.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Lektion 4 ist komplett: Lektions-Gate mit `00-lektions-gate.prompt.md`.
