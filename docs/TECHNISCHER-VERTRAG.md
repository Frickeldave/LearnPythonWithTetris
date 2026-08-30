# Technischer Vertrag

Der technische Vertrag legt nur fest, was die Kursprüfungen benötigen.
Er beschreibt **Schnittstellen** — keine Implementierung. Alles, was
hier nicht steht, darfst du frei gestalten.

## Allgemeines

- Deine Dateien liegen in `lernprojekt/`.
- Die Spiellogik soll ohne geöffnetes pygame-Fenster testbar sein.
- Die Kursprüfung lädt deine Module nur und führt Funktionen aus —
  sie verändert nichts.

## `settings.py` (Lektion 1)

| Name | Typ | Erwartung |
| ---- | --- | --------- |
| `BOARD_WIDTH` | int | 10 |
| `BOARD_HEIGHT` | int | 20 |

## `tetromino.py` (Lektion 2)

| Name | Typ | Erwartung |
| ---- | --- | --------- |
| `SHAPES` | Wörterbuch | Schlüssel genau: `I`, `O`, `T`, `S`, `Z`, `J`, `L` |
| `Tetromino` | Klasse | Konstruktor nimmt die Art entgegen |

`Tetromino`:

| Element | Erwartung |
| ------- | --------- |
| `kind` | die Art als Zeichenkette |
| `color` | die Farbe der Art; alle sieben Arten verschieden |
| `cells()` | Liste der Zellen `(x, y)` der aktuellen Form relativ zur Position; genau 4 Zellen |
| `rotate_cw()` | dreht im Uhrzeigersinn |
| `rotate_ccw()` | dreht gegen den Uhrzeigersinn und hebt die andere Richtung auf |

## `board.py` (Lektion 3)

`Board`:

| Element | Erwartung |
| ------- | --------- |
| `Board(10, 20)` | erzeugt ein Spielfeld |
| `width` / `height` | 10 und 20 |
| `grid` | Liste der Reihen; leere Zelle `None`, belegte Zelle speichert die Farbe |
| `is_inside(x, y)` | `True`, wenn innerhalb des Spielfelds |
| `cell_is_free(x, y)` | `True`, wenn frei; über dem Feld (y < 0) immer frei; links/rechts/unten nie frei |
| `can_place(cells, offset_x, offset_y)` | `True`, wenn alle Zellen der Form frei passen |
| `lock(cells, offset_x, offset_y, color)` | trägt die Zellen mit der Farbe ins Gitter ein |
| `full_lines()` | Liste aller vollständig gefüllten Reihen (y-Werte) |
| `clear_lines(lines)` | entfernt die Reihen, lässt alles darüber nachrutschen; gibt die Anzahl zurück |

## `game.py` (Lektionen 4–6)

`Game` (ohne pygame importierbar):

| Element | Erwartung |
| ------- | --------- |
| `board` | ein `Board`-Objekt |
| `active_piece` | der aktive `Tetromino` (oder `None` bei Game Over) |
| `next_piece` | der nächste `Tetromino` für die Vorschau |
| `piece_x` / `piece_y` | Position des aktiven Steins |
| `score`, `level`, `lines_cleared` | ganze Zahlen |
| `paused`, `game_over` | Wahrheitswerte |
| `move(dx)` | verschiebt um `dx` Spalten, wenn möglich |
| `soft_drop()` | ein Feld nach unten; 1 Punkt pro erfolgreichem Feld |
| `hard_drop()` | fällt sofort bis zum Boden (2 Punkte pro Feld) und fixiert |
| `rotate_cw()` / `rotate_ccw()` | drehen den aktiven Stein mit vereinfachtem Wall Kick |
| `tick()` | ein Schwerkraftschritt: fallen oder fixieren |
| `toggle_pause()` | schaltet die Pause um |
| `reset()` | setzt alles auf den Anfangszustand zurück |
| `fall_time()` | Sekunden pro Fallschritt; sinkt mit dem Level, nie unter 0,05 s |

## Punkte- und Levelregeln (Lektion 5)

- 1 Reihe: 100 × Level, 2 Reihen: 300 × Level, 3 Reihen: 500 × Level,
  4 Reihen: 800 × Level.
- Level = 1 + insgesamt entfernte Reihen // 10.

## Warum der Vertrag so klein ist

Je weniger vorgeschrieben ist, desto mehr eigene Lösungswege bleiben
dir. Die Kursprüfungen akzeptieren jede Umsetzung, die sich an diesen
Vertrag hält.
