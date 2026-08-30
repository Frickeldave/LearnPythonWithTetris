# Blockfall — Lerne Python mit Tetris

**Blockfall** ist ein einwöchiger Selbstlernkurs: Du baust mit Python
und pygame ein vollständiges Singleplayer-Blockspiel nach dem Vorbild
klassischer Tetris-Spiele — Schritt für Schritt, ohne Vorkenntnisse in
Spieleentwicklung.

Das Credo: **„Einfach, verständlich und vollständig."**

## Für wen ist der Kurs?

Für Jugendliche mit grundlegenden Python-Kenntnissen. Du brauchst:

- ein wenig Erfahrung mit Variablen, Schleifen und Bedingungen,
- einen Computer mit Windows, macOS oder Linux,
- ungefähr eine Stunde Zeit pro Tag für eine Woche.

## Was lernst du?

- ein Spiel von Grund auf planen und bauen
- pygame: Fenster, Eingabe, Zeichnen
- Datenstrukturen: Listen, Wörterbücher, Klassen
- Spiellogik sauber von der Darstellung trennen
- eigene automatische Tests schreiben
- Fehler systematisch untersuchen
- Code aufräumen und dokumentieren

## Wochenübersicht

| Tag | Inhalt |
| --- | ------ |
| Phase 0 | Vorbereitung: System einrichten, Referenzspiel kennenlernen |
| Lektion 1 | Fenster, Event-Loop, Spielfeld zeichnen |
| Lektion 2 | Tetrominos, aktiver Stein, 7-Bag, Vorschau |
| Lektion 3 | Bewegung, Spielfeldgrenzen, belegte Zellen, erste Tests |
| Lektion 4 | Schwerkraft, Fixieren, Rotation, Wall Kick |
| Lektion 5 | Reihen entfernen, Punkte, Level, Soft/Hard Drop |
| Lektion 6 | Anzeige, Pause, Game Over, Neustart — das Basisspiel ist fertig |
| Lektion 7 | Tests, Aufräumen, README, Abschlussprüfung |

Pro Lektion: 75–105 Minuten Basiszeit, höchstens 12 Stunden gesamt.
Bonusaufgaben zählen nicht dazu. Details: `docs/KURSPLAN.md`.

## Voraussetzungen und Einrichtung

Du brauchst Python ab 3.10 und pygame. Die Schritt-für-Schritt-Anleitung
für Windows, macOS und Linux steht in `docs/EINRICHTUNG.md`.

Kurzfassung:

```text
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows
# source .venv/bin/activate       # macOS / Linux
python -m pip install -r requirements.txt
python tools/check_environment.py
```

## Verzeichnisstruktur

| Verzeichnis | Zweck |
| ----------- | ----- |
| `lernprojekt/` | **Dein** Arbeitsbereich — hier entsteht dein Spiel |
| `referenzspiel/` | Vollständige Referenzlösung (für Übungen tabu) |
| `.github/` | Copilot-Instructions, Prompts, CI, Templates |
| `course_checks/` | Automatische Kursprüfungen je Lektion |
| `tools/` | Umgebungs-, Lektions- und Repository-Prüfung |
| `docs/` | Kursplan, Einrichtung, Leitfäden, Regeln |

Wichtig: Der Kurs kommt **ohne Git-Kenntnisse** aus. Es gibt keine
Branches — die Trennung von Lernprojekt und Referenzlösung passiert
ausschließlich über Verzeichnisse.

> Hinweis: Die Verzeichnistrennung ist keine technische Zugriffssperre.
> Du **kannst** `referenzspiel/` theoretisch öffnen — aber dann nimmst
> du dir selbst den Lernerfolg. In VS Code ist das Verzeichnis
> standardmäßig ausgeblendet (Hilfestellung, keine Sicherheitsfunktion).

## So startest du den Kurs

1. Richte dein System ein (`docs/EINRICHTUNG.md`).
2. Starte den Prompt `00-vorbereitung.prompt.md` in `.github/prompts/`
   mit GitHub Copilot: System prüfen, Namen nennen, Referenzspiel
   einmal spielen.
3. Danach: `00-kurs-start.prompt.md`, dann Lektion 1.

## Prompt-Dateien verwenden

Jede Übung hat eine eigene Prompt-Datei unter `.github/prompts/`
(z. B. `L03-E02-spielfeldgrenzen.prompt.md`). Du kopierst sie ins
Copilot-Chatfenster und arbeitest die Aufgabe **Schritt für Schritt**
ab. Copilot ist dein Lehrer: Er erklärt, fragt und prüft — den Code
schreibst **du**. Übersicht und Reihenfolge: `.github/prompts/README.md`.

## Lektions-Gates

Nach jeder Lektion prüft das Gate (Prompt `00-lektions-gate.prompt.md`),
ob du weiter darfst. Es kombiniert deine eigenen Tests
(`python -m unittest discover -s tests` in `lernprojekt/`) mit der
Kursprüfung:

```text
python tools/check_lesson.py --lesson 3
```

Mögliche Statuswerte: `BESTANDEN`, `NACHARBEIT ERFORDERLICH`,
`NICHT PRÜFBAR`. Bonusaufgaben gehören nie zum Gate.

## Hinweis auf das Referenzspiel

In `referenzspiel/` liegt die fertige Lösung — nur zum Kennenlernen in
Phase 0 und zur Wartung durch Kursverantwortliche gedacht. Für deine
Übungen gilt: **ausschließlich `lernprojekt/`**. Auch Copilot wird dir
aus dem Referenzspiel niemals etwas zeigen.

## Wichtige Dokumente

- `docs/KURSPLAN.md` — Ablauf und Zeitplan
- `docs/EINRICHTUNG.md` — Installation (Windows, macOS, Linux)
- `docs/LERNENDENLEITFADEN.md` — so funktioniert der Kurs
- `docs/KURSLEITUNGSLEITFADEN.md` — für Kursverantwortliche
- `docs/COPILOT-NUTZUNG.md` — Copilot als Lehrer nutzen
- `docs/SPIELREGELN.md` — Steuerung, Punkte, Level
- `docs/ARCHITEKTUR.md` — Aufbau des Spiels (konzeptionell)
- `docs/TECHNISCHER-VERTRAG.md` — Schnittstellen für die Kursprüfungen
- `docs/TESTEN.md` — eigene Tests schreiben
- `docs/FEHLERSUCHE.md` — häufige Probleme und Leitfragen
- `docs/ABNAHMETEST.md` — die vollständige Basisabnahme
- `docs/BONUSIDEEN.md` — freiwillige Erweiterungen
- `LEARNING_JOURNAL.md` — dein Lernjournal
- `PROGRESS.md` — deine Fortschrittsübersicht

Viel Spaß — und viel Erfolg beim Bauen deines eigenen Blockfall!