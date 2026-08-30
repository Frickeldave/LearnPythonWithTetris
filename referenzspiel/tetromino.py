"""Tetromino-Steine: Formen, Farben und Rotation.

Jeder Stein wird als kleines Rechteck aus Zeichen beschrieben:

    "X" bedeutet: Hier ist der Stein.
    "." bedeutet: Hier ist der Stein nicht.

Die Klasse `Tetromino` verwaltet eine Form und kann sie drehen.
"""

from settings import COLORS

# Jede Art hat eine eigene Form. Die Formen sind so gelegt, dass alle
# Steine in ein 3x3-Feld passen. Nur der I-Stein braucht ein 4x4-Feld.
SHAPES = {
    "I": [
        "....",
        "XXXX",
        "....",
        "....",
    ],
    "O": [
        "XX",
        "XX",
    ],
    "T": [
        ".X.",
        "XXX",
        "...",
    ],
    "S": [
        ".XX",
        "XX.",
        "...",
    ],
    "Z": [
        "XX.",
        ".XX",
        "...",
    ],
    "J": [
        "X..",
        "XXX",
        "...",
    ],
    "L": [
        "..X",
        "XXX",
        "...",
    ],
}


def _rotate_matrix(matrix, clockwise):
    """Dreht eine quadratische Zeichen-Matrix um 90 Grad."""
    size = len(matrix)
    if clockwise:
        return [
            "".join(matrix[size - 1 - x][y] for x in range(size))
            for y in range(size)
        ]
    return [
        "".join(matrix[x][size - 1 - y] for x in range(size))
        for y in range(size)
    ]


class Tetromino:
    """Ein Spielstein mit Art, Farbe, Form und Rotation."""

    def __init__(self, kind):
        if kind not in SHAPES:
            raise ValueError(f"Unbekannte Tetromino-Art: {kind}")
        self.kind = kind
        self.color = COLORS[kind]
        self.matrix = [row for row in SHAPES[kind]]

    def cells(self):
        """Liste aller Zellen (x, y) der aktuellen Form, relativ zur Position."""
        return [
            (x, y)
            for y, row in enumerate(self.matrix)
            for x, cell in enumerate(row)
            if cell == "X"
        ]

    def rotate_cw(self):
        """Dreht den Stein im Uhrzeigersinn."""
        self.matrix = _rotate_matrix(self.matrix, clockwise=True)

    def rotate_ccw(self):
        """Dreht den Stein gegen den Uhrzeigersinn."""
        self.matrix = _rotate_matrix(self.matrix, clockwise=False)
