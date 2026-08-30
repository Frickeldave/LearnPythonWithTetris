# L06 · B01 · Hold-Funktion

- **Lektion:** 6
- **Übung:** Bonus
- **Typ:** Bonus (freiwillig)
- **Dauer:** ca. 30 Minuten (zählt nicht zur Basiszeit)

> **Diese Aufgabe ist freiwillig und gehört nicht zum
> Vollständigkeits-Gate der nächsten Lektion.**

- **Voraussetzungen:** Lektion 6 (Basis) bestanden
- **Lernziel:** Du lagerst einen Stein auf „Halten": C legt den aktiven
  Stein zur Seite und holt einen früher gehaltenen zurück.
- **Sichtbares Ergebnis:** Ein Hold-Feld zeigt den gehaltenen Stein;
  C tauscht aktiven und gehaltenen Stein.
- **Betroffene Dateien:** `lernprojekt/game.py`, `lernprojekt/main.py`

## Aufgabe in kleinen Schritten

1. Lege einen Speicher für den gehaltenen Stein an (anfangs leer).
2. C tauscht aktiven und gehaltenen Stein.
3. Pro Fall eines Steins darf nur einmal gehalten werden — überlege
  dir, wie du das merkst und zurücksetzt.
4. Zeichne den gehaltenen Stein im Seitenbereich.
5. Achte auf den Sonderfall: erster Hold, wenn das Hold-Feld noch leer ist.

## Prüfen

**Manuell:** Hold tauscht korrekt; der gehaltene Stein ist sichtbar;
  pro Stein wirkt Hold nur einmal; nach Fixieren ist Hold wieder möglich.

## Definition of Done

- [ ] C tauscht aktiven und gehaltenen Stein.
- [ ] Der gehaltene Stein wird angezeigt.
- [ ] Pro fallendem Stein ist Hold nur einmal erlaubt.

## Verständnisfrage

Welche Zustände musst du dir für die Hold-Funktion merken?

## Für Copilot

Hinweisleiter verwenden, keine Lösungen liefern, keine Dateien ändern.
Bonus: darf jederzeit übersprungen werden.
