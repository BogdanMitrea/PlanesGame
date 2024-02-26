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
