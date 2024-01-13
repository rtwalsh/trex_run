import pygame
import random
from player import Player
from rock import Rock

BLACK = (0, 0, 0)

HEIGHT = 200
WIDTH = 640

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("T-Rex Run")

player = Player(20, 120)
obstacles = []
new_obstacle_delay = 0

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

        if new_obstacle_delay == 0 and random.random() > 0.8:
            obstacles.append(Rock(WIDTH, 150))
            new_obstacle_delay = 30

        player.update()
        for obstacle in obstacles:
            obstacle.update()

        player.draw(screen)
        remaining_obstacles = []
        for obstacle in obstacles:
            obstacle.draw(screen)

            if obstacle.x > 0:
                remaining_obstacles.append(obstacle)

        obstacles = remaining_obstacles
        if new_obstacle_delay > 0:
            new_obstacle_delay -= 1

        pygame.display.flip()
        clock.tick(30)

pygame.quit()