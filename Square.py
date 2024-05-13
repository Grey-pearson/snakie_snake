import pygame


class Square:
    def __init__(self, x, y, color, width, screen):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.screen = screen
        pass

    def draw_it(self):
        pygame.draw.rect(
            self.screen, self.color, (self.x, self.y, self.width, self.width), 0
        )
