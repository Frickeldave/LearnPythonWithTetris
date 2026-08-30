# L02 · E04 · Seven-Bag

- **Lektion:** 2
- **Übung:** 4 von 5
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 20 Minuten
- **Voraussetzungen:** Übung 3 bestanden
- **Lernziel:** Du sorgst für eine faire Zufallsreihenfolge: In jedem
  Durchgang von sieben Steinen kommt jede Art genau einmal vor.
- **Sichtbares Ergebnis:** Lässt du nacheinander viele Steine erzeugen,
  wiederholt sich in jedem Siebener-Paket keine Art.
- **Betroffene Dateien:** `lernprojekt/main.py` (oder eine passende
  eigene Datei)
- **Wichtige Begriffe:** Zufall, Liste, Mischen (`shuffle`), Beutel

## Aufgabe in kleinen Schritten

1. Lege eine Liste mit allen sieben Arten an — dein „Beutel".
2. Mische die Liste zu Beginn zufällig.
3. Nimm beim Erzeugen eines Steins immer die nächste Art aus dem Beutel.
4. Ist der Beutel leer, fülle und mische ihn neu.
5. Prüfe mit einer Ausgabe: In sieben aufeinanderfolgenden Steinen
   kommt keine Art doppelt vor.

## Unterstützung

- **Erlaubt:** Copilot erklärt `random.shuffle` und das Entnehmen aus Listen.
- **Verboten:** Keine fertige Beutel-Funktion.

## Prüfen

**Manuell:** Sieben nacheinander erzeugte Steine zeigen sieben
verschiedene Arten — in zufälliger Reihenfolge.

## Erwartetes Ergebnis

Ein 7-Bag-System: je sieben Steine enthält jede Art genau einmal.

## Definition of Done

- [ ] Ein Beutel mit allen sieben Arten existiert.
- [ ] Der Beutel wird zufällig gemischt.
- [ ] Steine werden aus dem Beutel entnommen.
- [ ] Ein leerer Beutel wird neu gefüllt und gemischt.

## Verständnisfrage

Warum ist das 7-Bag-System fairer als ein reiner Würfel pro Stein?

## Hinweisleiter

1. **Leitfrage:** Was passiert mit einer Liste, wenn du sie mischst?
2. **Konzeptueller Hinweis:** „Aus dem Beutel nehmen" = letztes Element
   entfernen.
3. **Algorithmus in Worten:** Beutel mischen, entnehmen, bei leerem
   Beutel neu füllen und mischen.
4. **Pseudocode:** wenn Beutel leer: füllen und mischen; dann entnehmen.
5. **Beispiel (max. 5 Zeilen):** Liste mischen und letztes Element nehmen.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L02-E05-vorschau.prompt.md`.
