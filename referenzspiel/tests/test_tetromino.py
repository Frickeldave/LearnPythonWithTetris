"""Tests für die Tetromino-Steine.

Ausführen aus dem Verzeichnis `referenzspiel/`:
    python -m unittest discover -s tests
"""

import unittest

from tetromino import SHAPES, Tetromino


class TestTetromino(unittest.TestCase):

    def test_alle_sieben_arten_vorhanden(self):
        self.assertEqual(
            set(SHAPES.keys()), {"I", "O", "T", "S", "Z", "J", "L"}
        )

    def test_jede_art_hat_vier_zellen(self):
        for kind in SHAPES:
            with self.subTest(kind=kind):
                self.assertEqual(len(Tetromino(kind).cells()), 4)

    def test_farben_sind_eindeutig(self):
        colors = {Tetromino(kind).color for kind in SHAPES}
        self.assertEqual(len(colors), 7)

    def test_rotation_veraendert_die_form(self):
        stone = Tetromino("T")
        before = stone.cells()
        stone.rotate_cw()
        self.assertNotEqual(stone.cells(), before)

    def test_viermal_drehen_ergibt_die_ausgangsform(self):
        stone = Tetromino("I")
        before = stone.cells()
        for _ in range(4):
            stone.rotate_cw()
        self.assertEqual(stone.cells(), before)

    def test_gegendrehung_hebt_drehung_auf(self):
        stone = Tetromino("L")
        before = stone.cells()
        stone.rotate_cw()
        stone.rotate_ccw()
        self.assertEqual(stone.cells(), before)

    def test_o_stein_bleibt_bei_rotation_gleich(self):
        stone = Tetromino("O")
        before = stone.cells()
        stone.rotate_cw()
        stone.rotate_ccw()
        self.assertEqual(stone.cells(), before)

    def test_unbekannte_art_fuehrt_zu_fehler(self):
        with self.assertRaises(ValueError):
            Tetromino("Q")


if __name__ == "__main__":
    unittest.main()
