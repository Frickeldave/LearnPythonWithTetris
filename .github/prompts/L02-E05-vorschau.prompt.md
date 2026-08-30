# L02 · E05 · Vorschau

- **Lektion:** 2
- **Übung:** 5 von 5
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 15 Minuten
- **Voraussetzungen:** Übung 4 bestanden
- **Lernziel:** Du zeigst neben dem Spielfeld den nächsten Stein als
  Vorschau an.
- **Sichtbares Ergebnis:** Rechts neben dem Feld ist immer der nächste
  Stein zu sehen; beim Fallen wechselt die Vorschau.
- **Betroffene Dateien:** `lernprojekt/main.py`
- **Wichtige Begriffe:** Vorschau, Seitenbereich, Reihenfolge von Zeichnen

## Aufgabe in kleinen Schritten

1. Merke dir den nächsten Stein getrennt vom aktiven Stein.
2. Wenn ein neuer Stein aktiv wird, bestimme sofort den übernächsten.
3. Verbreitere das Fenster für einen Seitenbereich.
4. Zeichne den nächsten Stein dort in einer kleinen Box.
5. Prüfe: Die Vorschau stimmt immer mit dem Stein überein, der als
   Nächstes fällt.

## Unterstützung

- **Erlaubt:** Copilot erklärt, wann im Ablauf die Vorschau neu
  bestimmt werden muss.
- **Verboten:** Keine fertige Vorschau-Zeichenfunktion.

## Prüfen

**Manuell:** Vorschau und tatsächlich fallender Stein stimmen immer überein.

## Erwartetes Ergebnis

Eine korrekte Vorschau des nächsten Steins im Seitenbereich.

## Definition of Done

- [ ] Der nächste Stein wird separat gespeichert.
- [ ] Die Vorschau wird bei jedem neuen Stein aktualisiert.
- [ ] Der Seitenbereich zeigt den nächsten Stein.
- [ ] Vorschau und fallender Stein stimmen überein.

## Verständnisfrage

Warum muss die Vorschau genau in dem Moment erneuert werden, in dem der
nächste Stein aktiv wird?

## Hinweisleiter

1. **Leitfrage:** Woher weiß dein Programm, welcher Stein als Nächstes kommt?
2. **Konzeptueller Hinweis:** „Aktiv machen" heißt: der nächste Stein
   wird zum aktiven — dann muss ein neuer nächster bestimmt werden.
3. **Algorithmus in Worten:** nächsten Stein erzeugen; wenn Stein aktiv
   wird, übernehmen und neuen nächsten erzeugen; Vorschau zeichnen.
4. **Pseudocode:** aktiver = nächster; nächster = neuer Stein.
5. **Beispiel (max. 5 Zeilen):** zwei Variablen, die Werte weiterreichen.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Lektion 2 ist komplett: Lektions-Gate mit `00-lektions-gate.prompt.md`.
