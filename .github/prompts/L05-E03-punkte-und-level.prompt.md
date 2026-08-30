# L05 · E03 · Punkte und Level

- **Lektion:** 5
- **Übung:** 3 von 5
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 25 Minuten
- **Voraussetzungen:** Übung 2 bestanden
- **Lernziel:** Dein Spiel zählt Punkte, entfernte Reihen und Level und
  wird mit jedem Level schneller.
- **Sichtbares Ergebnis:** Punktzahl, Reihen und Level werden angezeigt;
  die Fallgeschwindigkeit steigt mit dem Level.
- **Betroffene Dateien:** `lernprojekt/game.py` (oder deine Logik),
  `lernprojekt/settings.py`, `lernprojekt/main.py`
- **Wichtige Begriffe:** Punktzahl, Level, Zähler, Formel

## Aufgabe in kleinen Schritten

1. Lege die Punktwerte fest: 1 Reihe = 100, 2 = 300, 3 = 500,
   4 = 800 — jeweils multipliziert mit dem Level.
2. Zähle die insgesamt entfernten Reihen mit.
3. Berechne das Level: alle 10 entfernten Reihen ein Level höher.
4. Verkürze die Fallzeit mit steigendem Level — aber lege einen
  Mindestwert fest, damit es nie unspielbar wird.
5. Teste deine Rechnung mit ein paar Beispielwerten.

## Unterstützung

- **Erlaubt:** Copilot erklärt die Punkteformel und das Absichern eines Mindestwerts.
- **Verboten:** Keine fertige Punkte-Funktion.

## Prüfen

**Manuell:** Schließt du eine Reihe ab, steigen Punkte und Reihenzähler.
  Nach 10 Reihen steigt das Level, und das Fallen wird schneller.
**Automatisch:** eigene Tests zu den Formeln.

## Erwartetes Ergebnis

Punkte, Reihen, Level und Geschwindigkeit hängen korrekt zusammen.

## Definition of Done

- [ ] Punktwerte 100/300/500/800 × Level sind umgesetzt.
- [ ] Die entfernten Reihen werden insgesamt gezählt.
- [ ] Alle 10 Reihen steigt das Level.
- [ ] Die Fallzeit sinkt mit dem Level und hat einen Mindestwert.
- [ ] Punkte, Reihen und Level werden angezeigt.

## Verständnisfrage

Warum multiplizierst du die Punkte mit dem Level — und warum gibt es
eine Mindestfallzeit?

## Hinweisleiter

1. **Leitfrage:** Wie hängt die Fallzeit vom Level ab — und wo darf
  sie nicht hinkommen?
2. **Konzeptueller Hinweis:** `max(...)` begrenzt eine Berechnung nach unten.
3. **Algorithmus in Worten:** Reihen addieren, Level berechnen, Fallzeit
  aus Level berechnen und begrenzen.
4. **Pseudocode:** level = 1 + reihen // 10; fallzeit = max(basis − …, minimum).
5. **Beispiel (max. 5 Zeilen):** `max`-Ausdruck mit zwei Werten.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L05-E04-soft-drop.prompt.md`.
