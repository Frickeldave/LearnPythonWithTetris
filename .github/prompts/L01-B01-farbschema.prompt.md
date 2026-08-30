# L01 · B01 · Farbschema

- **Lektion:** 1
- **Übung:** Bonus
- **Typ:** Bonus (freiwillig)
- **Dauer:** ca. 20 Minuten (zählt nicht zur Basiszeit)

> **Diese Aufgabe ist freiwillig und gehört nicht zum
> Vollständigkeits-Gate der nächsten Lektion.**

- **Voraussetzungen:** Lektion 1 (Basis) bestanden
- **Lernziel:** Du gestaltest ein eigenes Farbschema und lagerst Farben
  vollständig in `settings.py` aus.
- **Sichtbares Ergebnis:** Dein Spielfeld trägt dein eigenes Farbschema.
- **Betroffene Dateien:** `lernprojekt/settings.py`, `lernprojekt/main.py`

## Aufgabe in kleinen Schritten

1. Notiere, welche Farben dein Spiel haben soll (Hintergrund, Linien).
2. Suche passende RGB-Werte für deine Farben.
3. Trage alle Farben als Konstanten in `settings.py` ein.
4. Ersetze in `main.py` jede direkt geschriebene Farbe durch die Konstante.

## Prüfen

**Manuell:** Das Spielfeld zeigt dein Farbschema; in `main.py` stehen
keine direkten Farbwerte mehr.

## Definition of Done

- [ ] Alle Farben stehen in `settings.py`.
- [ ] `main.py` benutzt nur noch die Konstanten.
- [ ] Das Spiel läuft weiterhin fehlerfrei.

## Verständnisfrage

Was ist leichter zu ändern, wenn eine Farbe nur an einer Stelle steht?

## Für Copilot

Hinweisleiter verwenden, keine Lösungen liefern, keine Dateien ändern.
Bonus: darf jederzeit übersprungen werden.
