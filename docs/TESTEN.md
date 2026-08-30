# Testen im Blockfall-Kurs

Es gibt zwei Sorten von Prüfungen:

| Prüfung | Wo | Wer schreibt sie | Zweck |
| ------- | -- | ---------------- | ----- |
| Eigene Tests | `lernprojekt/tests/` | du selbst | Deine Spiellogik absichern |
| Kursprüfungen | `course_checks/` + `tools/` | der Kurs | Lektionsstand feststellen |

Beide ergänzen sich: Die Kursprüfung ersetzt deine eigenen Tests nicht,
und deine Tests ersetzen nicht die Kursprüfung.

## Grundlagen von `unittest`

Ein Test ist eine Klasse mit Methoden, deren Namen mit `test_` beginnen.
In jeder Testmethode vergleichst du das tatsächliche Ergebnis mit deiner
Erwartung.

## Arrange, Act, Assert

Jeder gute Test hat drei Phasen:

1. **Arrange** — alles vorbereiten (Objekte erzeugen, Werte setzen).
2. **Act** — die zu testende Aktion ausführen.
3. **Assert** — prüfen, ob das Ergebnis der Erwartung entspricht.

## Testen ohne pygame-Fenster

Damit Tests ohne Fenster laufen, hältst du die Spiellogik getrennt von
pygame (siehe `docs/ARCHITEKTUR.md`):

- `board.py`, `tetromino.py` und `game.py` importieren **kein** pygame.
- `main.py` importiert pygame und steuert Fenster, Eingabe und Zeichnen.
- Deine Tests importieren nur die Logik-Module.

## Tests ausführen

Im Verzeichnis `lernprojekt/`:

```text
python -m unittest discover -s tests
```

Alle Tests grün? Dann zeigt unittest `OK`. Bei Fehlern meldet es,
welcher Test in welcher Zeile gescheitert ist — lies die Meldung genau.

## Typische Testfälle für Blockfall

Diese Liste soll dich inspirieren, nicht ersetzen:

- jede Tetromino-Art hat genau 4 Zellen,
- alle sieben Farben sind verschieden,
- viermal im Uhrzeigersinn drehen ergibt die Ausgangsform,
- eine Zelle innerhalb des Felds ist frei, außerhalb nicht,
- über dem Spielfeld ist alles frei,
- nach `lock` sind die Zellen belegt,
- eine volle Reihe wird erkannt und entfernt,
- nach dem Entfernen rutscht der Inhalt nach,
- `move` verändert die Position, `soft_drop` gibt 1 Punkt,
- `reset` setzt Punkte, Level und Zustand zurück.

Schreibe deine Tests selbst — Copilot beschreibt dir Testfälle gern
in Worten, liefert aber keinen Testcode.
