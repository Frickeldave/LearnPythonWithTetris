"""Das Spielfeld: ein Raster aus Zellen.

Jede Zelle ist entweder leer (`None`) oder enthält die Farbe eines
fixierten Steins. Diese Datei benutzt kein pygame und lässt sich
deshalb gut mit Tests überprüfen.
"""

from settings import BOARD_HEIGHT, BOARD_WIDTH


class Board:
    """Ein Spielfeld mit `width` Spalten und `height` Reihen."""

    def __init__(self, width=BOARD_WIDTH, height=BOARD_HEIGHT):
        self.width = width
        self.height = height
        self.clear()

    def clear(self):
        """Macht alle Zellen leer."""
        self.grid = [[None] * self.width for _ in range(self.height)]

    def is_inside(self, x, y):
        """True, wenn (x, y) innerhalb des Spielfelds liegt."""
        return 0 <= x < self.width and 0 <= y < self.height

    def cell_is_free(self, x, y):
        """True, wenn die Zelle frei ist.

        Über dem Spielfeld (y < 0) ist alles frei, damit neue Steine
        von oben hereinfallen können. Links, rechts und unterhalb des
        Spielfelds ist nichts frei.
        """
        if x < 0 or x >= self.width:
            return False
        if y < 0:
            return True
        if y >= self.height:
            return False
        return self.grid[y][x] is None

    def can_place(self, cells, offset_x, offset_y):
        """True, wenn alle Zellen der Form frei auf das Feld passen."""
        return all(
            self.cell_is_free(offset_x + cell_x, offset_y + cell_y)
            for cell_x, cell_y in cells
        )

    def lock(self, cells, offset_x, offset_y, color):
        """Trägt die Zellen der Form mit der Farbe in das Feld ein."""
        for cell_x, cell_y in cells:
            x = offset_x + cell_x
            y = offset_y + cell_y
            if self.is_inside(x, y):
                self.grid[y][x] = color

    def full_lines(self):
        """Liste der Reihen (y-Werte), die vollständig gefüllt sind."""
        return [y for y, row in enumerate(self.grid) if all(row)]

    def clear_lines(self, lines):
        """Entfernt die Reihen und lässt alles darüber nachrutschen."""
        for y in sorted(lines, reverse=True):
            del self.grid[y]
        for _ in lines:
            self.grid.insert(0, [None] * self.width)
        return len(lines)
