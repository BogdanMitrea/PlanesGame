import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Button:

    def __init__(self, x, y, width, height, color, text, border_color=None, border_width=0):
        uifont = pygame.font.Font(None, 18)
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.surface = uifont.render(text, True, (0, 0, 0))
        self.surface_rect = self.surface.get_rect(center=self.rect.center)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(self.surface, self.surface_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def draw_table(screen, x, y, headrows, headcols, rows, cols, clicked_cell):
    CELL_SIZE = 25
    TABLE_WIDTH = 10 * CELL_SIZE
    TABLE_HEIGHT = 10 * CELL_SIZE
    for col in range(1, 11):
        label = chr(ord('A') + col - 1)
        font = pygame.font.SysFont(None, 24)
        text = font.render(label, True, (255, 255, 255))
        screen.blit(text, (col * CELL_SIZE + 0.5 * CELL_SIZE - 6 + x, 5 + y))

    # Draw row labels (1 to 10)
    for row in range(1, 11):
        label = str(row)
        font = pygame.font.SysFont(None, 24)
        text = font.render(label, True, (255, 255, 255))
        screen.blit(text, (5 + x, row * CELL_SIZE + 0.5 * CELL_SIZE - 12 + y))

    for row in range(10):
        for col in range(10):
            if clicked_cell[row][col]:
                pygame.draw.rect(screen, (0, 255, 0),
                                 ((col + 1) * CELL_SIZE + x, (row + 1) * CELL_SIZE + y, CELL_SIZE, CELL_SIZE), 1)
            else:
                pygame.draw.rect(screen, (0, 0, 0),
                                 ((col + 1) * CELL_SIZE + x, (row + 1) * CELL_SIZE + y, CELL_SIZE, CELL_SIZE), 1)

    uifont = pygame.font.SysFont(None, 16)
    if headrows != None:
        for i in range(len(headrows)):
            x_text = uifont.render("H", True, (255, 255, 255))
            screen.blit(x_text, (int(headrows[i] + 1) * 25 + 10 + x, int(headcols[i] + 1) * 25 + 8 + y))
        for i in range(len(rows)):
            if not (rows[i] == headrows[0] and cols[i] == headcols[0]) and not (
                    rows[i] == headrows[1] and cols[i] == headcols[1]) and not (
                    rows[i] == headrows[2] and cols[i] == headcols[2]):
                x_text = uifont.render("x", True, (255, 255, 255))
                screen.blit(x_text, (int(rows[i] + 1) * 25 + 10 + x, int(cols[i] + 1) * 25 + 8 + y))

def get_cell_from_mouse(pos, x, y):
    CELL_SIZE = 25
    x1, y1 = pos[0] - x, pos[1] - y
    col = x1 // CELL_SIZE
    row = y1 // CELL_SIZE
    if 0 < col <= 10 and 0 < row <= 10:
        return row, col
    return None
