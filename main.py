import pygame
from player import Player
from rock import Rock

BLACK = (0, 0, 0)

HEIGHT = 200
WIDTH = 640

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("T-Rex Run")

player = Player(20, 120)
rock = Rock(WIDTH, 150)

clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            player.jump()

    if not done:
        screen.fill(BLACK)

        player.update()
        rock.update()

        player.draw(screen)
        rock.draw(screen)

        pygame.display.flip()
        clock.tick(60)

pygame.quit()