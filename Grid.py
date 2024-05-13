import Square
import pygame

x = 900
y = 600
screen = pygame.display.set_mode((x, y))
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (211, 211, 211)


class Grid:
    def __init__(self, grid_size, distance_between_squares, color):
        self.grid_size = grid_size
        self.distance_between_squares = distance_between_squares
        self.color = color
        self.square = []
        x = 0
        y = 0

        for i in range(self.grid_size * 2):
            square = Square(20, 20, GREEN, 20, screen)
