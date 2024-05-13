import pygame
import pygame.display
from Square import Square

# set up
pygame.init()
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()
running = True
dt = 0
FPS = 60
# colors for bodie ig
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (211, 211, 211)

# snake_head = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("purple")
    # start

    # square.draw_it()

    # end
    # puts work on screen?
    pygame.display.flip()
    # limit FPS to 60, prolly should be lower
    dt = clock.tick(FPS) / 1000

pygame.quit()
