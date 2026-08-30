"""Tests für das Spielfeld (Board).

Ausführen aus dem Verzeichnis `referenzspiel/`:
    python -m unittest discover -s tests
"""

import unittest

from board import Board


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board(10, 20)

    def test_feldgroesse(self):
        self.assertEqual(self.board.width, 10)
        self.assertEqual(self.board.height, 20)
        self.assertEqual(len(self.board.grid), 20)
        self.assertTrue(all(len(row) == 10 for row in self.board.grid))

    def test_is_inside(self):
        self.assertTrue(self.board.is_inside(0, 0))
        self.assertTrue(self.board.is_inside(9, 19))
        self.assertFalse(self.board.is_inside(-1, 0))
        self.assertFalse(self.board.is_inside(10, 0))
        self.assertFalse(self.board.is_inside(0, 20))

    def test_anfangs_ist_alles_frei(self):
        self.assertTrue(self.board.cell_is_free(5, 5))

    def test_ueber_dem_feld_ist_frei(self):
        self.assertTrue(self.board.cell_is_free(0, -1))
        self.assertFalse(self.board.cell_is_free(-1, -1))
        self.assertFalse(self.board.cell_is_free(10, -1))

    def test_lock_traegt_farbe_ein(self):
        color = (255, 0, 0)
        self.board.lock([(0, 0), (1, 0)], 3, 4, color)
        self.assertEqual(self.board.grid[4][3], color)
        self.assertEqual(self.board.grid[4][4], color)

    def test_can_place_und_belegte_zellen(self):
        cells = [(0, 0), (1, 0)]
        self.assertTrue(self.board.can_place(cells, 0, 0))
        self.board.lock(cells, 0, 0, (0, 0, 255))
        self.assertFalse(self.board.can_place(cells, 0, 0))
        self.assertFalse(self.board.can_place(cells, -1, 0))
        self.assertTrue(self.board.can_place(cells, 0, 1))

    def test_full_lines_erkennt_volle_reihen(self):
        for x in range(10):
            self.board.grid[19][x] = (1, 1, 1)
        self.assertEqual(self.board.full_lines(), [19])

    def test_clear_lines_entfernt_und_lasst_nachrutschen(self):
        color = (1, 2, 3)
        for y in (18, 19):
            for x in range(10):
                self.board.grid[y][x] = color
        self.board.grid[0][0] = color
        removed = self.board.clear_lines([18, 19])
        self.assertEqual(removed, 2)
        # Der Stein aus Reihe 0 ist zwei Reihen nach unten gerutscht.
        self.assertEqual(self.board.grid[2][0], color)
        self.assertTrue(all(cell is None for cell in self.board.grid[19]))

    def test_clear_setzt_das_feld_zurueck(self):
        self.board.lock([(0, 0)], 5, 5, (9, 9, 9))
        self.board.clear()
        self.assertTrue(
            all(cell is None for row in self.board.grid for cell in row)
        )


if __name__ == "__main__":
    unittest.main()
