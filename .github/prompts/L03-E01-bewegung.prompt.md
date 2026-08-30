# L03 · E01 · Bewegung

- **Lektion:** 3
- **Übung:** 1 von 4
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 20 Minuten
- **Voraussetzungen:** Lektion 2 bestanden
- **Lernziel:** Du bewegst den aktiven Stein mit den Pfeiltasten nach
  links und rechts.
- **Sichtbares Ergebnis:** Links/Rechts-Tasten verschieben den Stein
  um eine Spalte pro Tastendruck.
- **Betroffene Dateien:** `lernprojekt/main.py`
- **Wichtige Begriffe:** Tastatur-Event, Taste, Verschieben

## Aufgabe in kleinen Schritten

1. Erkenne in der Event-Schleife die Tasten Pfeil links und Pfeil rechts.
2. Ändere bei jedem Tastendruck die x-Position des Steins um ±1.
3. Lass den Stein nicht bei gedrückter Taste „rasen" — ein Druck soll
   genau einen Schritt auslösen (Tipp: `KEYDOWN`-Ereignis).
4. Teste beidseitig: ein Tastendruck, ein Feld.

## Unterstützung

- **Erlaubt:** Copilot erklärt den Unterschied zwischen „Taste gedrückt"
  und „Taste gedrückt gehalten".
- **Verboten:** Keine fertige Bewegungsfunktion.

## Prüfen

**Manuell:** Jeder Druck auf Links/Rechts verschiebt den Stein genau
eine Spalte. Der Stein verschwindet dabei nicht aus dem Bild.

## Erwartetes Ergebnis

Stein reagiert auf Links und Rechts mit genau einem Feld pro Druck.

## Definition of Done

- [ ] Pfeil links verschiebt um eine Spalte nach links.
- [ ] Pfeil rechts verschiebt um eine Spalte nach rechts.
- [ ] Ein Tastendruck löst genau einen Schritt aus.
- [ ] Der Stein wird an der neuen Position gezeichnet.

## Verständnisfrage

Warum benutzt du für Bewegung das Ereignis „Taste wurde gedrückt"
und nicht „Taste ist gedrückt"?

## Hinweisleiter

1. **Leitfrage:** Welches Ereignis meldet dir einen einzelnen Tastendruck?
2. **Konzeptueller Hinweis:** Position ändern heißt: den x-Wert neu
   berechnen und danach neu zeichnen.
3. **Algorithmus in Worten:** Taste erkennen, x-Wert anpassen, Zeichnen
   wiederholen.
4. **Pseudocode:** wenn Taste links: x um 1 verringern.
5. **Beispiel (max. 5 Zeilen):** Bedingung, die eine Variable verändert.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L03-E02-spielfeldgrenzen.prompt.md`.
