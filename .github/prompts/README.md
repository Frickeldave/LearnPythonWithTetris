# Prompt-Dateien des Blockfall-Kurses

Hier liegen die Prompt-Dateien, die den Kurs steuern. Eine Prompt-Datei
ist eine Aufgabenbeschreibung, die du gemeinsam mit GitHub Copilot
durcharbeitest.

## Wie starte ich einen Prompt?

1. Öffne die gewünschte `.prompt.md`-Datei.
2. Kopiere ihren Inhalt in das Chat-Fenster von GitHub Copilot
   (oder hänge die Datei als Kontext an).
3. Arbeite die Aufgabe mit Copilot Schritt für Schritt durch.
   Copilot erklärt immer nur den nächsten kleinen Schritt.

> Wichtig: Die Prompts dürfen keine fertigen Lösungen enthalten — du
> schreibst deinen Code selbst. Copilot darf dir helfen, aber nichts
> in `lernprojekt/` für dich schreiben.

## Empfohlene Reihenfolge

| Reihenfolge | Prompt | Typ | Zeit |
| ----------- | ------ | --- | ---- |
| 1 | `00-vorbereitung.prompt.md` | Vorbereitung | ca. 45–60 Min |
| 2 | `00-kurs-start.prompt.md` | Einstieg | ca. 15 Min |
| 3 | `L01-E01` … `L01-E05` | Basis | ca. 95 Min |
| 4 | `00-lektions-gate.prompt.md` (Lektion 1) | Gate | ca. 15 Min |
| 5 | `L02-E01` … `L02-E05` | Basis | ca. 95 Min |
| 6 | `00-lektions-gate.prompt.md` (Lektion 2) | Gate | ca. 15 Min |
| 7 | `L03-E01` … `L03-E04` | Basis | ca. 90 Min |
| 8 | `00-lektions-gate.prompt.md` (Lektion 3) | Gate | ca. 15 Min |
| 9 | `L04-E01` … `L04-E04` | Basis | ca. 95 Min |
| 10 | `00-lektions-gate.prompt.md` (Lektion 4) | Gate | ca. 15 Min |
| 11 | `L05-E01` … `L05-E05` | Basis | ca. 100 Min |
| 12 | `00-lektions-gate.prompt.md` (Lektion 5) | Gate | ca. 15 Min |
| 13 | `L06-E01` … `L06-E05` | Basis | ca. 90 Min |
| 14 | `00-lektions-gate.prompt.md` (Lektion 6) | Gate | ca. 15 Min |
| 15 | `L07-E01` … `L07-E04` | Basis | ca. 100 Min |
| 16 | `00-lektions-gate.prompt.md` (Lektion 7) | Gate | ca. 15 Min |
| 17 | `00-abschlusspruefung.prompt.md` | Abschluss | ca. 30 Min |

Grundregel: Basisaufgaben (`E`) sind Pflicht, Bonusaufgaben (`B`) sind
freiwillig und gehören nie zu einem Gate.

## Übergeordnete Prompts

| Datei | Zweck |
| ----- | ----- |
| `00-vorbereitung.prompt.md` | System einrichten, Name erfragen, Referenzspiel kennenlernen |
| `00-kurs-start.prompt.md` | Kursbeginn: Wochenplan, Arbeitsbereich, Rollen |
| `00-lektions-gate.prompt.md` | Prüfung am Ende einer Lektion |
| `00-debugging.prompt.md` | Fehler gemeinsam untersuchen |
| `00-code-review.prompt.md` | Code auf Verständlichkeit prüfen |
| `00-abschlusspruefung.prompt.md` | Vollständige Basisabnahme |

## Zuordnung zu den Lektionen

- **Lektion 1:** Fenster, Event-Loop, Spielfeld — `L01-E01` bis `L01-E05`
- **Lektion 2:** Tetrominos, aktiver Stein, 7-Bag, Vorschau — `L02-E01` bis `L02-E05`
- **Lektion 3:** Bewegung, Grenzen, belegte Zellen, Tests — `L03-E01` bis `L03-E04`
- **Lektion 4:** Schwerkraft, Fixieren, Rotation, Wall Kick — `L04-E01` bis `L04-E04`
- **Lektion 5:** Reihen, Punkte, Level, Soft/Hard Drop — `L05-E01` bis `L05-E05`
- **Lektion 6:** Anzeige, Pause, Game Over, Neustart, Hinweise — `L06-E01` bis `L06-E05`
- **Lektion 7:** Tests, Aufräumen, README, Abnahme — `L07-E01` bis `L07-E04`

## Bonusaufgaben

Jede Bonus-Datei beginnt mit `B` (z. B. `L05-B01-ghost-piece.prompt.md`).
Bonusaufgaben:

- beginnen erst nach bestandener Basislektion,
- sind keine Voraussetzung für spätere Übungen,
- dürfen jederzeit übersprungen werden,
- zählen nicht zur Basiszeit,
- beeinflussen die Abschlussbewertung nicht.

## Abweichung von der ursprünglichen Planung

Zusätzlich zur ursprünglichen Struktur existiert der Prompt
`00-vorbereitung.prompt.md` (Phase 0). Er ist der erste Schritt des
Kurses und bereitet System und Person auf die sieben Lektionen vor.
