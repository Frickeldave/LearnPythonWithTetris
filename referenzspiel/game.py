"""Die Spiellogik: Steine fallen, Reihen verschwinden, Punkte zählen.

Diese Datei benutzt bewusst KEIN pygame, damit die Logik einfach
mit automatischen Tests überprüft werden kann.
"""

import random

from board import Board
from settings import (
    BASE_FALL_TIME,
    LINES_PER_LEVEL,
    MIN_FALL_TIME,
    SCORE_DOUBLE,
    SCORE_HARD_DROP,
    SCORE_SINGLE,
    SCORE_SOFT_DROP,
    SCORE_TETRIS,
    SCORE_TRIPLE,
    SPEEDUP_PER_LEVEL,
)
from tetromino import SHAPES, Tetromino

# Punkte je nach Anzahl gleichzeitig entfernter Reihen.
LINE_SCORES = {
    1: SCORE_SINGLE,
    2: SCORE_DOUBLE,
    3: SCORE_TRIPLE,
    4: SCORE_TETRIS,
}

# Vereinfachter Wall Kick: Nach einer Rotation wird zuerst die aktuelle
# Position geprüft, dann ein Feld nach links, ein Feld nach rechts und
# ein Feld nach oben. Bewusst einfacher als ein offizielles
# Tetris-Rotationssystem.
WALL_KICKS = [(0, 0), (-1, 0), (1, 0), (0, -1)]


class Game:
    """Der komplette Spielzustand ohne Grafik."""

    def __init__(self):
        self.board = Board()
        self.reset()

    # ------------------------------------------------------------------
    # Start und Neustart
    # ------------------------------------------------------------------
    def reset(self):
        """Setzt das Spiel in den Anfangszustand zurück."""
        self.board.clear()
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.game_over = False
        self.paused = False
        self.bag = []
        self.active_piece = None
        self.next_piece = None
        self.piece_x = 0
        self.piece_y = 0
        self._spawn_next()
        self._spawn_active()

    # ------------------------------------------------------------------
    # 7-Bag: Alle sieben Steine kommen in zufälliger Reihenfolge,
    # bevor sich der Vorrat wieder auffüllt.
    # ------------------------------------------------------------------
    def _refill_bag(self):
        self.bag = list(SHAPES.keys())
        random.shuffle(self.bag)

    def take_from_bag(self):
        if not self.bag:
            self._refill_bag()
        return self.bag.pop()

    def _spawn_next(self):
        self.next_piece = Tetromino(self.take_from_bag())

    def _spawn_active(self):
        """Macht den nächsten Stein aktiv. Blockiert er sofort, ist das Spiel aus."""
        self.active_piece = self.next_piece
        self.piece_x = self.board.width // 2 - 2
        self.piece_y = 0
        if not self.board.can_place(
            self.active_piece.cells(), self.piece_x, self.piece_y
        ):
            self.game_over = True
            self.active_piece = None
        else:
            self._spawn_next()

    # ------------------------------------------------------------------
    # Bewegung
    # ------------------------------------------------------------------
    def move(self, dx):
        """Verschiebt den aktiven Stein um dx Spalten. Gibt Erfolg zurück."""
        if self.game_over or self.paused or self.active_piece is None:
            return False
        new_x = self.piece_x + dx
        if self.board.can_place(self.active_piece.cells(), new_x, self.piece_y):
            self.piece_x = new_x
            return True
        return False

    def soft_drop(self):
        """Bewegt den Stein ein Feld nach unten und gibt einen Punkt."""
        if self.game_over or self.paused or self.active_piece is None:
            return False
        if self._step_down():
            self.score += SCORE_SOFT_DROP
            return True
        return False

    def hard_drop(self):
        """Lässt den Stein sofort ganz nach unten fallen und fixiert ihn."""
        if self.game_over or self.paused or self.active_piece is None:
            return
        distance = 0
        while self._step_down():
            distance += 1
        self.score += distance * SCORE_HARD_DROP
        self._lock_active()

    def _step_down(self):
        """Ein Feld nach unten, wenn möglich. Gibt Erfolg zurück."""
        if self.board.can_place(
            self.active_piece.cells(), self.piece_x, self.piece_y + 1
        ):
            self.piece_y += 1
            return True
        return False

    # ------------------------------------------------------------------
    # Rotation mit vereinfachtem Wall Kick
    # ------------------------------------------------------------------
    def rotate_cw(self):
        """Dreht den aktiven Stein im Uhrzeigersinn."""
        return self._rotate(clockwise=True)

    def rotate_ccw(self):
        """Dreht den aktiven Stein gegen den Uhrzeigersinn."""
        return self._rotate(clockwise=False)

    def _rotate(self, clockwise):
        if self.game_over or self.paused or self.active_piece is None:
            return False
        if clockwise:
            self.active_piece.rotate_cw()
        else:
            self.active_piece.rotate_ccw()
        if self._try_kicks():
            return True
        # Kein Kick hat gepasst: Rotation zurücknehmen.
        if clockwise:
            self.active_piece.rotate_ccw()
        else:
            self.active_piece.rotate_cw()
        return False

    def _try_kicks(self):
        for dx, dy in WALL_KICKS:
            x = self.piece_x + dx
            y = self.piece_y + dy
            if self.board.can_place(self.active_piece.cells(), x, y):
                self.piece_x = x
                self.piece_y = y
                return True
        return False

    # ------------------------------------------------------------------
    # Schwerkraft
    # ------------------------------------------------------------------
    def fall_time(self):
        """Sekunden pro Fallschritt im aktuellen Level."""
        return max(
            BASE_FALL_TIME - (self.level - 1) * SPEEDUP_PER_LEVEL,
            MIN_FALL_TIME,
        )

    def tick(self):
        """Ein Schwerkraftschritt: fallen oder fixieren."""
        if self.game_over or self.paused or self.active_piece is None:
            return
        if not self._step_down():
            self._lock_active()

    # ------------------------------------------------------------------
    # Fixieren, Reihen entfernen, Punkte und Level
    # ------------------------------------------------------------------
    def _lock_active(self):
        self.board.lock(
            self.active_piece.cells(),
            self.piece_x,
            self.piece_y,
            self.active_piece.color,
        )
        removed = self.board.clear_lines(self.board.full_lines())
        if removed:
            self.lines_cleared += removed
            self.score += LINE_SCORES.get(removed, 0) * self.level
            self.level = 1 + self.lines_cleared // LINES_PER_LEVEL
        self._spawn_active()

    # ------------------------------------------------------------------
    # Pause
    # ------------------------------------------------------------------
    def toggle_pause(self):
        if not self.game_over:
            self.paused = not self.paused
