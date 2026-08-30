"""Blockfall — das Referenzspiel.

Starte das Spiel aus diesem Verzeichnis mit:

    python main.py

Steuerung:
    Pfeil links / rechts   Stein bewegen
    Pfeil unten            Soft Drop (weiches Fallen)
    Pfeil oben oder X      im Uhrzeigersinn drehen
    Z                      gegen den Uhrzeigersinn drehen
    Leertaste              Hard Drop (sofort fallen lassen)
    P                      Pause
    R                      Neustart
    Escape                 Spiel beenden
"""

import pygame

from game import Game
from settings import (
    BOARD_HEIGHT,
    BOARD_WIDTH,
    CELL_SIZE,
    COLOR_BACKGROUND,
    COLOR_GAME_OVER,
    COLOR_GRID,
    COLOR_SIDEBAR,
    COLOR_TEXT,
    SIDEBAR_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)

BOARD_PIXEL_WIDTH = BOARD_WIDTH * CELL_SIZE
BOARD_PIXEL_HEIGHT = BOARD_HEIGHT * CELL_SIZE


class BlockfallApp:
    """Verbindet pygame mit der Spiellogik: Eingabe, Update, Zeichnen."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Blockfall")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 28)
        self.font_small = pygame.font.Font(None, 20)
        self.game = Game()
        self.fall_timer = 0.0

    # ------------------------------------------------------------------
    # Hauptschleife
    # ------------------------------------------------------------------
    def run(self):
        running = True
        while running:
            dt = self.clock.tick(60) / 1000.0
            running = self.handle_events()
            self.update(dt)
            self.draw()
        pygame.quit()

    # ------------------------------------------------------------------
    # Eingabe
    # ------------------------------------------------------------------
    def handle_events(self):
        """Verarbeitet alle Ereignisse. False beendet das Spiel."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                self.handle_key(event.key)
        return True

    def handle_key(self, key):
        if key == pygame.K_LEFT:
            self.game.move(-1)
        elif key == pygame.K_RIGHT:
            self.game.move(1)
        elif key == pygame.K_DOWN:
            self.game.soft_drop()
        elif key == pygame.K_UP or key == pygame.K_x:
            self.game.rotate_cw()
        elif key == pygame.K_z:
            self.game.rotate_ccw()
        elif key == pygame.K_SPACE:
            self.game.hard_drop()
        elif key == pygame.K_p:
            self.game.toggle_pause()
        elif key == pygame.K_r:
            self.game.reset()

    # ------------------------------------------------------------------
    # Update: Schwerkraft nach Zeit
    # ------------------------------------------------------------------
    def update(self, dt):
        if self.game.paused or self.game.game_over:
            return
        self.fall_timer += dt
        while self.fall_timer >= self.game.fall_time():
            self.fall_timer -= self.game.fall_time()
            self.game.tick()

    # ------------------------------------------------------------------
    # Zeichnen
    # ------------------------------------------------------------------
    def draw(self):
        self.screen.fill(COLOR_BACKGROUND)
        self.draw_board()
        self.draw_sidebar()
        if self.game.paused:
            self.draw_center_text("PAUSE", COLOR_TEXT)
            self.draw_center_text("P = weiterspielen", COLOR_TEXT, y_offset=40)
        if self.game.game_over:
            self.draw_center_text("GAME OVER", COLOR_GAME_OVER)
            self.draw_center_text("R = Neustart", COLOR_TEXT, y_offset=40)
        pygame.display.flip()

    def draw_board(self):
        board = self.game.board
        for y in range(board.height):
            for x in range(board.width):
                color = board.grid[y][x]
                if color is not None:
                    self.draw_cell(x, y, color)
        if self.game.active_piece is not None:
            for cell_x, cell_y in self.game.active_piece.cells():
                self.draw_cell(
                    self.game.piece_x + cell_x,
                    self.game.piece_y + cell_y,
                    self.game.active_piece.color,
                )
        for x in range(board.width + 1):
            pygame.draw.line(
                self.screen, COLOR_GRID,
                (x * CELL_SIZE, 0), (x * CELL_SIZE, BOARD_PIXEL_HEIGHT),
            )
        for y in range(board.height + 1):
            pygame.draw.line(
                self.screen, COLOR_GRID,
                (0, y * CELL_SIZE), (BOARD_PIXEL_WIDTH, y * CELL_SIZE),
            )

    def draw_cell(self, x, y, color):
        rect = pygame.Rect(
            x * CELL_SIZE + 1, y * CELL_SIZE + 1,
            CELL_SIZE - 2, CELL_SIZE - 2,
        )
        pygame.draw.rect(self.screen, color, rect)

    def draw_sidebar(self):
        rect = pygame.Rect(BOARD_PIXEL_WIDTH, 0, SIDEBAR_WIDTH, WINDOW_HEIGHT)
        pygame.draw.rect(self.screen, COLOR_SIDEBAR, rect)
        x = BOARD_PIXEL_WIDTH + 20
        self.draw_text(f"Punkte: {self.game.score}", x, 20)
        self.draw_text(f"Level: {self.game.level}", x, 60)
        self.draw_text(f"Reihen: {self.game.lines_cleared}", x, 100)
        self.draw_text("Nächster Stein:", x, 160)
        self.draw_next_piece(x, 190)
        controls = [
            "Links/Rechts: bewegen",
            "Unten: Soft Drop",
            "Oben oder X: drehen",
            "Z: andersherum drehen",
            "Leertaste: Hard Drop",
            "P: Pause",
            "R: Neustart",
            "Esc: Beenden",
        ]
        y = 260
        for line in controls:
            self.draw_small_text(line, x, y)
            y += 24

    def draw_next_piece(self, x, y):
        if self.game.next_piece is None:
            return
        for cell_x, cell_y in self.game.next_piece.cells():
            rect = pygame.Rect(
                x + cell_x * CELL_SIZE, y + cell_y * CELL_SIZE,
                CELL_SIZE - 2, CELL_SIZE - 2,
            )
            pygame.draw.rect(self.screen, self.game.next_piece.color, rect)

    def draw_text(self, text, x, y, color=COLOR_TEXT):
        image = self.font.render(text, True, color)
        self.screen.blit(image, (x, y))

    def draw_small_text(self, text, x, y, color=COLOR_TEXT):
        image = self.font_small.render(text, True, color)
        self.screen.blit(image, (x, y))

    def draw_center_text(self, text, color, y_offset=0):
        image = self.font.render(text, True, color)
        rect = image.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + y_offset)
        )
        self.screen.blit(image, rect)


if __name__ == "__main__":
    BlockfallApp().run()
