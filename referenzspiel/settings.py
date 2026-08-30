"""Zentrale Einstellungen des Referenzspiels.

Alle wichtigen Zahlen und Farben stehen hier an einer Stelle,
damit sie leicht zu finden und zu ändern sind.
"""

# ---------------------------------------------------------------------------
# Spielfeld
# ---------------------------------------------------------------------------
BOARD_WIDTH = 10           # Spalten
BOARD_HEIGHT = 20          # sichtbare Reihen

# ---------------------------------------------------------------------------
# Darstellung (alles in Pixeln)
# ---------------------------------------------------------------------------
CELL_SIZE = 30             # Kantenlänge einer Zelle
SIDEBAR_WIDTH = 200        # Breite der Seitenanzeige rechts neben dem Feld
WINDOW_WIDTH = BOARD_WIDTH * CELL_SIZE + SIDEBAR_WIDTH
WINDOW_HEIGHT = BOARD_HEIGHT * CELL_SIZE

# ---------------------------------------------------------------------------
# Fallgeschwindigkeit (Sekunden pro Fallschritt)
# ---------------------------------------------------------------------------
BASE_FALL_TIME = 0.8       # Fallzeit in Level 1
MIN_FALL_TIME = 0.05       # Die Fallzeit darf nie unter diesen Wert sinken
SPEEDUP_PER_LEVEL = 0.08   # So viel wird das Spiel pro Level schneller

# ---------------------------------------------------------------------------
# Level und Punkte
# ---------------------------------------------------------------------------
LINES_PER_LEVEL = 10       # Nach so vielen Reihen steigt das Level

SCORE_SINGLE = 100         # Punkte für 1 gleichzeitig entfernte Reihe
SCORE_DOUBLE = 300         # Punkte für 2 Reihen
SCORE_TRIPLE = 500         # Punkte für 3 Reihen
SCORE_TETRIS = 800         # Punkte für 4 Reihen
SCORE_SOFT_DROP = 1        # Punkte pro Feld beim weichen Fallen
SCORE_HARD_DROP = 2        # Punkte pro Feld beim harten Fallen

# ---------------------------------------------------------------------------
# Farben (Rot, Grün, Blau) für die sieben Tetromino-Arten
# ---------------------------------------------------------------------------
COLORS = {
    "I": (0, 240, 240),    # Cyan
    "O": (240, 240, 0),    # Gelb
    "T": (160, 0, 240),    # Lila
    "S": (0, 240, 0),      # Grün
    "Z": (240, 0, 0),      # Rot
    "J": (0, 0, 240),      # Blau
    "L": (240, 160, 0),    # Orange
}

# ---------------------------------------------------------------------------
# Farben der Oberfläche
# ---------------------------------------------------------------------------
COLOR_BACKGROUND = (20, 20, 30)
COLOR_GRID = (60, 60, 70)
COLOR_TEXT = (230, 230, 230)
COLOR_SIDEBAR = (35, 35, 45)
COLOR_GAME_OVER = (240, 80, 80)
