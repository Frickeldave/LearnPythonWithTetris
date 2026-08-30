# Spielregeln: Blockfall

Blockfall ist ein Singleplayer-Blockspiel nach dem Vorbild klassischer
Tetris-Spiele.

## Ziel

Baue vollständige Reihen, damit sie verschwinden. Das Spiel endet,
wenn ein neuer Stein keinen Platz mehr findet.

## Spielfeld

- 10 Spalten und 20 sichtbare Reihen
- Die Steine erscheinen oben in der Mitte und fallen nach unten.

## Die sieben Steine

Jede der sieben Arten hat ihre eigene Farbe:

| Art | Form-Beschreibung | Farbe |
| --- | ----------------- | ----- |
| I | langer Balken | Cyan |
| O | Quadrat | Gelb |
| T | T-Form | Lila |
| S | S-Form | Grün |
| Z | Z-Form | Rot |
| J | J-Form | Blau |
| L | L-Form | Orange |

Die Reihenfolge der Steine ist fair gelost: In jedem Paket von sieben
Steinen kommt jede Art genau einmal vor (7-Bag-System).

## Steuerung

| Taste | Wirkung |
| ----- | ------- |
| Pfeil links / rechts | Stein bewegen |
| Pfeil unten | Soft Drop (weich fallen, 1 Punkt pro Feld) |
| Pfeil oben oder X | im Uhrzeigersinn drehen |
| Z | gegen den Uhrzeigersinn drehen |
| Leertaste | Hard Drop (sofort fallen lassen, 2 Punkte pro Feld) |
| P | Pause |
| R | Neustart (auch nach Game Over) |
| Escape | Spiel beenden |

## Wall Kick

Passt ein gedrehter Stein nicht an seine Position, probiert das Spiel
ein Feld nach links, ein Feld nach rechts und ein Feld nach oben.
Das ist bewusst einfacher als ein offizielles Tetris-Rotationssystem.

## Punkte

| Aktion | Punkte |
| ------ | ------ |
| 1 Reihe entfernt | 100 × Level |
| 2 Reihen entfernt | 300 × Level |
| 3 Reihen entfernt | 500 × Level |
| 4 Reihen entfernt | 800 × Level |
| Soft Drop | 1 pro Feld |
| Hard Drop | 2 pro Feld |

## Level und Geschwindigkeit

- Start bei Level 1.
- Nach jeweils **zehn** insgesamt entfernten Reihen steigt das Level.
- Mit jedem Level fällt der Stein schneller — bis zu einer
  Mindestfallzeit, damit das Spiel nie unspielbar wird.

## Spielende und Neustart

- Das Spiel endet, wenn ein neuer Stein an seiner Startposition
  blockiert ist.
- Mit R startest du ein neues Spiel, ohne das Programm zu schließen.
- Escape beendet das Programm sauber.
