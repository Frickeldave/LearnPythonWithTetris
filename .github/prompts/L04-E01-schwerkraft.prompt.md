# L04 · E01 · Schwerkraft

- **Lektion:** 4
- **Übung:** 1 von 4
- **Typ:** Basis (Pflicht)
- **Dauer:** ca. 20 Minuten
- **Voraussetzungen:** Lektion 3 bestanden
- **Lernziel:** Der Stein fällt von selbst in gleichmäßigen Abständen
  nach unten.
- **Sichtbares Ergebnis:** Ohne Tastendruck fällt der Stein langsam
  und gleichmäßig — ein Feld pro Zeitspanne.
- **Betroffene Dateien:** `lernprojekt/main.py` (Logik gern in
  `game.py` oder ähnlich), `lernprojekt/settings.py`
- **Wichtige Begriffe:** Zeitschritt, Takt, `pygame.time.Clock`,
  `get_ticks`, Konstante

## Aufgabe in kleinen Schritten

1. Lege eine Fallzeit fest (z. B. 0,8 Sekunden pro Feld) — als
  Konstante in `settings.py`.
2. Miss die vergangene Zeit seit dem letzten Fallschritt.
3. Ist die Fallzeit erreicht, bewege den Stein ein Feld nach unten
  und beginne die Messung neu.
4. Verwende dabei dieselbe „erst prüfen, dann bewegen"-Regel wie bei
  der Bewegung.
5. Teste: Der Stein fällt flüssig, nicht ruckartig.

## Unterstützung

- **Erlaubt:** Copilot erklärt Zeitmessung und Taktgeber.
- **Verboten:** Keine fertige Update-Funktion.

## Prüfen

**Manuell:** Der Stein fällt ohne Eingabe gleichmäßig ein Feld pro
Fallzeit (etwa 0,8 Sekunden).

## Erwartetes Ergebnis

Zeitgesteuerte Schwerkraft mit konstanter Fallgeschwindigkeit.

## Definition of Done

- [ ] Eine Fallzeit ist als Konstante festgelegt.
- [ ] Die Zeit seit dem letzten Schritt wird gemessen.
- [ ] Nach Ablauf der Fallzeit fällt der Stein ein Feld.
- [ ] Die Fallprüfung nutzt die Kollisionsregeln aus Lektion 3.

## Verständnisfrage

Warum misst man Zeit mit einem Taktgeber, statt einfach pro
Schleifendurchlauf zu fallen?

## Hinweisleiter

1. **Leitfrage:** Woher weißt du, wie viel Zeit vergangen ist?
2. **Konzeptueller Hinweis:** Auf schnellen Rechnern läuft die Schleife
   unterschiedlich oft pro Sekunde — Zeit ist der faire Takt.
3. **Algorithmus in Worten:** Zeit aufsammeln; wenn genug Zeit: Schritt
   nach unten versuchen; Zeitkonto zurücksetzen.
4. **Pseudocode:** timer += vergangene Zeit; solange timer ≥ fallzeit:
   fallen; timer −= fallzeit.
5. **Beispiel (max. 5 Zeilen):** Variable, die Zeit aufsummiert.

## Für Copilot

Prüfe die Voraussetzungen, erkläre nur den ersten Schritt, warte auf die
Umsetzung, prüfe danach den Stand. Keine Datei verändern, keine Lösung
liefern. Sprich die Person mit ihrem Namen an, sobald er bekannt ist.

## Abschluss und nächster Schritt

Weiter mit `L04-E02-fixieren.prompt.md`.
