# L05 · E02 · Reihen entfernen

- **Lektion:** 5
- **Übung:** 2 von 5
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 25 Minuten
- **Voraussetzungen:** Übung 1 bestanden
- **Lernziel:** Volle Reihen verschwinden, und alles darüber rutscht
  nach unten.
- **Sichtbares Ergebnis:** Schließt du eine Reihe ab, verschwindet sie,
  und der Rest des Stapels rutscht eine Reihe tiefer.
- **Betroffene Dateien:** `lernprojekt/board.py`, `lernprojekt/main.py`
- **Wichtige Begriffe:** Entfernen, Nachrutschen, Einfügen

## Aufgabe in kleinen Schritten

1. Entferne jede volle Reihe aus dem Gitter.
2. Füge für jede entfernte Reihe oben eine neue leere Reihe ein.
3. Achte auf die Reihenfolge: Entferne von unten nach oben, damit
  sich die Nummern nicht verschieben.
4. Rufe diese Funktion in deinem Spiellauf auf, wenn ein Stein fixiert wird.
5. Teste: Einzelne und mehrere Reihen gleichzeitig, auch ganz oben
  und ganz unten im Feld.

## Unterstützung

- **Erlaubt:** Copilot erklärt `del`, `insert` und warum die Reihenfolge zählt.
- **Verboten:** Keine fertige Entfernen-Funktion.

## Prüfen

**Manuell:** Eine vollständige Reihe verschwindet sofort, der Stapel
rutscht sauber nach. **Automatisch:** eigene Tests laufen grün.

## Erwartetes Ergebnis

Volle Reihen werden entfernt; das Feld rutscht korrekt nach.

## Definition of Done

- [ ] Volle Reihen werden aus dem Gitter entfernt.
- [ ] Oben werden gleich viele leere Reihen eingefügt.
- [ ] Die Entfernung läuft von unten nach oben.
- [ ] Mehrere Reihen gleichzeitig funktionieren.
- [ ] Das Entfernen wird nach dem Fixieren ausgelöst.

## Verständnisfrage

Warum ist die Reihenfolge beim Entfernen (unten zuerst) so wichtig?

## Hinweisleiter

1. **Leitfrage:** Was passiert mit den Zeilennummern, wenn du eine
  Reihe entfernst?
2. **Konzeptueller Hinweis:** Von unten nach oben bleiben die Nummern
  der noch zu entfernenden Reihen stabil.
3. **Algorithmus in Worten:** Reihen sortieren, von unten entfernen,
  oben leere Reihen einfügen.
4. **Pseudocode:** für jede volle Reihe (absteigend): entfernen; dann
  oben auffüllen.
5. **Beispiel (max. 5 Zeilen):** `del` auf einer Liste mit Index.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L05-E03-punkte-und-level.prompt.md`.
