"""Tests für die zentrale Spiellogik.

Die Spiellogik benutzt kein pygame, deshalb laufen diese Tests
ohne geöffnetes Fenster.

Ausführen aus dem Verzeichnis `referenzspiel/`:
    python -m unittest discover -s tests
"""

import unittest

from game import Game
from settings import (
    BOARD_WIDTH,
    LINES_PER_LEVEL,
    MIN_FALL_TIME,
    SCORE_SINGLE,
)
from tetromino import Tetromino


class TestGameLogic(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_startzustand(self):
        self.assertFalse(self.game.game_over)
        self.assertFalse(self.game.paused)
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.level, 1)
        self.assertEqual(self.game.lines_cleared, 0)
        self.assertIsNotNone(self.game.active_piece)
        self.assertIsNotNone(self.game.next_piece)

    def test_move_links_und_rechts(self):
        start_x = self.game.piece_x
        self.assertTrue(self.game.move(-1))
        self.assertEqual(self.game.piece_x, start_x - 1)
        self.assertTrue(self.game.move(1))
        self.assertEqual(self.game.piece_x, start_x)

    def test_move_stoppt_an_der_wand(self):
        for _ in range(BOARD_WIDTH):
            self.game.move(-1)
        min_x = min(cell_x for cell_x, _ in self.game.active_piece.cells())
        self.assertGreaterEqual(self.game.piece_x + min_x, 0)

    def test_soft_drop_bewegt_und_gibt_punkte(self):
        y = self.game.piece_y
        self.assertTrue(self.game.soft_drop())
        self.assertEqual(self.game.piece_y, y + 1)
        self.assertEqual(self.game.score, 1)

    def test_hard_drop_fixiert_und_erzeugt_neuen_stein(self):
        self.game.hard_drop()
        self.assertTrue(
            any(
                cell is not None
                for row in self.game.board.grid
                for cell in row
            )
        )
        self.assertIsNotNone(self.game.active_piece)

    def test_tick_faellt_bis_zum_boden_und_fixiert(self):
        for _ in range(40):
            self.game.tick()
        self.assertIsNotNone(self.game.active_piece)
        self.assertTrue(
            any(
                cell is not None
                for row in self.game.board.grid
                for cell in row
            )
        )

    def test_rotation_an_der_wand_wird_gekickt(self):
        for _ in range(BOARD_WIDTH):
            self.game.move(-1)
        self.assertTrue(self.game.rotate_cw())
        min_x = min(cell_x for cell_x, _ in self.game.active_piece.cells())
        self.assertGreaterEqual(self.game.piece_x + min_x, 0)

    def test_pause_stoppt_die_schwerkraft(self):
        self.game.toggle_pause()
        self.assertTrue(self.game.paused)
        y = self.game.piece_y
        self.game.tick()
        self.assertEqual(self.game.piece_y, y)
        self.game.toggle_pause()
        self.assertFalse(self.game.paused)

    def test_reset_setzt_alles_zurueck(self):
        self.game.soft_drop()
        self.game.hard_drop()
        self.game.reset()
        self.assertEqual(self.game.score, 0)
        self.assertEqual(self.game.level, 1)
        self.assertEqual(self.game.lines_cleared, 0)
        self.assertFalse(self.game.game_over)
        self.assertFalse(self.game.paused)
        self.assertIsNotNone(self.game.active_piece)

    def test_seven_bag_liefert_alle_arten(self):
        # Ein frischer Beutel liefert genau die sieben Arten, bevor er sich auffüllt.
        self.game.bag = []
        kinds = [self.game.take_from_bag() for _ in range(7)]
        self.assertEqual(sorted(kinds), ["I", "J", "L", "O", "S", "T", "Z"])

    def test_eine_reihe_gibt_punkte(self):
        # Der I-Stein fällt 18 Felder (2 Punkte pro Feld) und schließt
        # anschließend eine Reihe ab (100 Punkte in Level 1).
        self._complete_one_line()
        self.assertEqual(self.game.lines_cleared, 1)
        self.assertEqual(self.game.score, 18 * 2 + SCORE_SINGLE)

    def test_nach_zehn_reihen_steigt_das_level(self):
        for _ in range(LINES_PER_LEVEL):
            self._complete_one_line()
        self.assertEqual(self.game.lines_cleared, LINES_PER_LEVEL)
        self.assertEqual(self.game.level, 2)

    def test_fallzeit_sinkt_mit_dem_level_und_hat_minimum(self):
        self.game.level = 1
        langsam = self.game.fall_time()
        self.game.level = 3
        schneller = self.game.fall_time()
        self.assertLess(schneller, langsam)
        self.game.level = 99
        self.assertEqual(self.game.fall_time(), MIN_FALL_TIME)

    def test_game_over_bei_blockiertem_start(self):
        # Sind die obersten Reihen blockiert, kann kein neuer Stein erscheinen.
        for y in range(2):
            for x in range(BOARD_WIDTH):
                self.game.board.grid[y][x] = (1, 1, 1)
        self.game.next_piece = Tetromino("T")
        self.game._spawn_active()
        self.assertTrue(self.game.game_over)
        self.assertIsNone(self.game.active_piece)

    def test_neustart_nach_game_over(self):
        for y in range(2):
            for x in range(BOARD_WIDTH):
                self.game.board.grid[y][x] = (1, 1, 1)
        self.game.next_piece = Tetromino("T")
        self.game._spawn_active()
        self.assertTrue(self.game.game_over)
        self.game.reset()
        self.assertFalse(self.game.game_over)
        self.assertIsNotNone(self.game.active_piece)

    def _complete_one_line(self):
        """Füllt die letzte Reihe bis auf vier Spalten und schließt sie mit einem I-Stein."""
        for x in range(4, BOARD_WIDTH):
            self.game.board.grid[19][x] = (1, 1, 1)
        # Spalten 0 bis 3 bleiben frei — dort landet der waagerechte I-Stein.
        self.game.active_piece = Tetromino("I")
        self.game.piece_x = 0
        self.game.piece_y = 0
        self.game.hard_drop()


if __name__ == "__main__":
    unittest.main()
