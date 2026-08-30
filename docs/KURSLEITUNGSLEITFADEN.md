# Leitfaden für Kursleitungen

Dieser Leitfaden erklärt Aufbau, Ablauf und Pflege des Blockfall-Kurses
für Kursverantwortliche und Betreuende.

## Verzeichnisstruktur

| Verzeichnis | Zweck |
| ----------- | ----- |
| `lernprojekt/` | Arbeitsbereich der Lernenden — anfangs leer |
| `referenzspiel/` | Vollständige, getestete Referenzimplementierung |
| `.github/` | Copilot-Instructions, Prompts, CI, Templates |
| `course_checks/` | Kursprüfungen je Lektion |
| `tools/` | Umgebungs-, Lektions- und Repository-Prüfung |
| `docs/` | Kursdokumentation |

## Zweck von `lernprojekt/`

Im Lernbetrieb ist `lernprojekt/` der einzige Arbeitsbereich. Die
Lernenden erstellen dort `main.py`, `settings.py`, `tetromino.py`,
`board.py`, `game.py`, eigene Tests und eine eigene README.

Der Ausgangszustand enthält bewusst **keinen** Lösungscode, keine
Gerüste und keine TODOs.

## Zweck von `referenzspiel/`

Das Referenzspiel dient:

- als Kontrolle der Kursverantwortlichen („das Ziel ist erreichbar"),
- den Lernenden in Phase 0 zum Kennenlernen des Spiels,
- der CI als Testobjekt.

Im Lernbetrieb ist es für Copilot tabu; Lernende sollen es nicht
öffnen (VS Code blendet es standardmäßig aus, `.vscode/settings.json`).

## Zeitplanung

- Phase 0 (Vorbereitung): ca. 45–60 Minuten, außerhalb der Basiszeit.
- Sieben Lektionen à 75–105 Minuten, höchstens 12 Stunden gesamt.
- Nach jeder Lektion: Lektions-Gate.
- Nach Lektion 6 ist das Basisspiel spielbar; Lektion 7 ist Testen,
  Aufräumen, Dokumentieren und Abnahme.

## Kursprüfungen nutzen

```text
python tools/check_lesson.py --lesson 1
...
python tools/check_lesson.py --lesson 7
python tools/check_lesson.py --lesson all
```

Exit-Codes: 0 = `BESTANDEN`, 1 = `NACHARBEIT ERFORDERLICH`,
2 = `NICHT PRÜFBAR`. Die Prüfungen verändern `lernprojekt/` nicht
und prüfen nie Bonusaufgaben. Der erforderliche technische Vertrag
(Funktionsnamen) steht in `docs/TECHNISCHER-VERTRAG.md`.

## Typische Probleme

- **Python fehlt oder ist zu alt** → `tools/check_environment.py`
  früh laufen lassen.
- **virtuelle Umgebung nicht aktiv** → Prompt `(.venv)` prüfen.
- **Fenster reagiert nicht** → Event-Schleife prüfen; typischerweise
  fehlt `pygame.event.get()` oder `flip()`.
- **Tests importieren Module nicht** → Tests aus `lernprojekt/` heraus
  starten: `python -m unittest discover -s tests`.
- **Frustration durch zu viel Hilfe** → auf Hinweisleiter bestehen;
  Copilot springt nicht zur Lösung.

## Mögliche Vereinfachungen

- Bonusaufgaben komplett weglassen.
- Lektion 7 auf Tests und Abnahme verkürzen, wenn Zeit fehlt.
- Die Lektions-Gates können mit `--lesson all` am Ende gesammelt
  nachgeholt werden.

## Abschlussabnahme

Die vollständige Basisabnahme läuft über
`00-abschlusspruefung.prompt.md` und `docs/ABNAHMETEST.md`. Nur wenn
alle Basistests grün sind, alle Pflichtfunktionen vorhanden sind, die
manuellen Prüfungen bestätigt wurden und die Verständnisfragen
beantwortet sind, gilt das Projekt als abgeschlossen.

## Grenzen der rein verzeichnisbasierten Trennung

Die Trennung von `lernprojekt/` und `referenzspiel/` ist **keine
technische Zugriffssperre**. Lernende können `referenzspiel/`
theoretisch öffnen. Die Trennung soll Bedienung vereinfachen,
versehentliches Kopieren verhindern und Git-Kenntnisse überflüssig
machen. Das Ausblenden in VS Code ist nur Hilfestellung; der Kurs
funktioniert auch ohne VS Code.

## Pflege

Änderungen am Referenzspiel, an Prüfungen oder Prompts gehören zur
administrativen Wartung (siehe `CONTRIBUTING.md`). Die Namensdatei
`lernender-name.txt` ist lokal und darf nie eingecheckt werden.
