# Leitfaden für Lernende

## So funktioniert der Kurs

In einer Woche baust du mit Python und pygame dein eigenes Spiel:
**Blockfall** — ein Tetris-artiges Blockspiel. Du arbeitest dich Übung
für Übung durch die Prompts im Ordner `.github/prompts/`.

Das Wichtigste zuerst:

- Du arbeitest **ausschließlich** im Verzeichnis `lernprojekt/`.
- **Jede Zeile Code schreibst du selbst.** Das ist das Lernziel.
- GitHub Copilot ist dein Lehrer, nicht dein Entwickler.

## Wie starte ich eine Übung?

1. Öffne die passende Prompt-Datei in `.github/prompts/`
   (z. B. `L03-E01-bewegung.prompt.md`).
2. Kopiere den Inhalt ins Copilot-Chatfenster (oder hänge die Datei an).
3. Arbeite die Aufgabe **Schritt für Schritt** ab. Copilot erklärt
   immer nur den nächsten kleinen Schritt.

Die empfohlene Reihenfolge steht in `.github/prompts/README.md`.

## Wie nutze ich Copilot als Lehrer?

Copilot darf dir helfen bei:

- Konzepten und Begriffen,
- Zerlegen einer Aufgabe in kleine Schritte,
- Verständnisfragen,
- Hinweisen und Pseudocode,
- Fehlermeldungen erklären,
- deinen Code ansehen und prüfen,
- Tests und Kursprüfungen ausführen.

Copilot darf **nicht**:

- deinen Projektcode schreiben oder ändern,
- Dateien in `lernprojekt/` anlegen,
- dir die fertige Lösung geben — auch nicht, wenn du direkt danach fragst,
- in `referenzspiel/` nachsehen und dir von dort Lösungen zeigen.

## Warum schreibt Copilot keinen Code für mich?

Abgetippter Code bleibt fremder Code. Wenn du jede Zeile selbst
schreibst, verstehst du, was passiert — und genau das ist das Ziel.
Deshalb verwendet Copilot bei Problemen die **Hinweisleiter**:

1. Leitfrage
2. konzeptueller Hinweis
3. Algorithmus in Worten
4. kurzer Pseudocode
5. allgemeines Beispiel (höchstens fünf Zeilen)

Nach jeder Stufe versuchst du es selbst — erst dann geht es weiter.

## Dein Name

Zu Beginn fragt Copilot nach deinem Namen und merkt ihn sich in der
lokalen Datei `lernender-name.txt` (im Wurzelverzeichnis, in
`.gitignore`). Danach spricht Copilot dich mit Namen an. Möchtest du
keinen Namen angeben, sag es einfach — dann ist „du" völlig in Ordnung.
Dein Name landet niemals in Git oder in eingecheckten Dateien.

## Gates: Habe ich die Lektion geschafft?

Nach jeder Lektion prüft das Lektions-Gate (Prompt
`00-lektions-gate.prompt.md`), ob du bereit für die nächste Lektion
bist. Es nutzt deine eigenen Tests und die Kursprüfung:

```text
python tools/check_lesson.py --lesson 3
```

Mögliche Ergebnisse:

| Status | Bedeutung |
| ------ | --------- |
| `BESTANDEN` | Weiter zur nächsten Lektion |
| `NACHARBEIT ERFORDERLICH` | Etwas fehlt oder ist fehlerhaft |
| `NICHT PRÜFBAR` | Dateien fehlen oder sind nicht startbar |

## Fehler untersuchen

Wenn etwas nicht funktioniert: Ruhe bewahren, Prompt
`00-debugging.prompt.md` verwenden und Copilot die **vollständige**
Fehlermeldung zeigen. Häufige Probleme stehen in `docs/FEHLERSUCHE.md`.

## Bonusaufgaben

Bonusaufgaben (Dateien mit `B`) sind freiwillig. Bearbeite sie erst
nach bestandener Basislektion — oder überspringe sie ganz. Sie zählen
nicht zur Zeit und nicht zur Bewertung.

## Dein Fortschritt

Halte deine Lernerfahrungen in `LEARNING_JOURNAL.md` fest und hake
deine Lektionen in `PROGRESS.md` ab. Trage dort **keine persönlichen
Daten** wie deinen Namen ein — diese Dateien werden mit Git gespeichert.
