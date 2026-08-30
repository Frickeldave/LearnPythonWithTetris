# GitHub Copilot im Kurs nutzen

## Rolle von Copilot

Copilot ist im Blockfall-Kurs ein **geduldiger Python- und
pygame-Lehrer** — kein Entwickler deines Projekts. Die Regeln stehen in
`.github/copilot-instructions.md` und in den pfadspezifischen Dateien
unter `.github/instructions/`.

## Was Copilot nicht tun darf

- Projektcode schreiben oder Dateien in `lernprojekt/` anlegen/ändern,
- vollständige Funktionen, Klassen, Dateien oder Tests liefern,
- TODOs ausfüllen oder Diffs mit Lösungen erzeugen,
- eine korrigierte Komplettversion deines Codes ausgeben,
- `referenzspiel/` lesen, durchsuchen, zitieren oder übertragen.

Das gilt auch dann, wenn du ausdrücklich nach der fertigen Lösung fragst.
Die einzige Ausnahme: Copilot darf die lokale Datei
`lernender-name.txt` anlegen — nur den Namen, nur mit deiner Zustimmung.

## Wie starte ich eine Prompt-Datei?

1. Öffne die `.prompt.md`-Datei (z. B. `L04-E03-rotation.prompt.md`).
2. Kopiere ihren Inhalt ins Copilot-Chatfenster — oder füge die Datei
   über „Kontext hinzufügen" an.
3. Folge den Anweisungen. Copilot erklärt nur den nächsten kleinen Schritt
   und wartet auf deine Umsetzung.

## Wie stelle ich eine gute Lernfrage?

Gute Fragen führen schneller zum Ziel:

- **Konkret statt allgemein:** „Warum bleibt mein Stein bei x = −1
  stehen?" statt „Mein Code geht nicht."
- **Erwartung benennen:** Was hätte passieren sollen?
- **Beobachtung benennen:** Was passiert stattdessen?
- **Code zeigen:** den betroffenen Ausschnitt aus `lernprojekt/`.

## Wie gebe ich eine Fehlermeldung weiter?

Kopiere den **vollständigen** Traceback — von der ersten bis zur
letzten Zeile, ohne Kürzungen. Bei abgestürzten Spielen zählt auch die
Ausgabe im Terminal.

## Wie fordere ich ein Code-Review an?

Verwende den Prompt `00-code-review.prompt.md`. Copilot prüft deinen
Code auf Verständlichkeit, Namen, kurze Funktionen, doppelte Logik,
magische Zahlen und Testbarkeit — und nennt Verbesserungen, die **du**
umsetzt.

## Dein Name

Copilot fragt zu Kursbeginn nach deinem Namen und speichert ihn lokal
in `lernender-name.txt` (Wurzelverzeichnis, in `.gitignore`). Solange
die Datei existiert, spricht Copilot dich mit Namen an. Möchtest du
keinen Namen angeben, ist das in Ordnung — dann bleibt es bei „du".

## Kursprüfungen durch Copilot

Copilot darf Kursprüfungen ausführen und erklären, z. B.:

```text
python tools/check_lesson.py --lesson 3
```

Er darf deine eigenen Tests starten und Testergebnisse erläutern —
aber niemals Tests für dich schreiben.
