import pygame
from tile import *

BLACK = (0, 0, 0)

HEIGHT = 200
WIDTH = 640

TILE_HEIGHT = 50
TILE_WIDTH = 50

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("T-Rex Run")

tile = Tile(20, 120, TILE_WIDTH, TILE_HEIGHT)

clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            tile.jump()

    if not done:
        screen.fill(BLACK)

        tile.update()
        tile.draw(screen)

        pygame.display.flip()
        clock.tick(60)

pygame.quit()