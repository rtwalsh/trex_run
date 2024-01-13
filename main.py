import pygame
import random
from player import Player
from obstacle import Obstacle
from colors import *

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.jump()
            elif event.key == pygame.K_RIGHT:
                Obstacle.speed_up()
            elif event.key == pygame.K_LEFT:
                Obstacle.slow_down()

    if not done:
        screen.fill(BLACK)

        if new_obstacle_delay == 0 and random.random() > 0.8:
            if random.choice(["rock", "cactus"]) == "rock":
                obstacles.append(Obstacle(WIDTH, 150, "rock.png"))
            else:
                obstacles.append(Obstacle(WIDTH, 130, "cactus.png"))
            new_obstacle_delay = 30

        player.update()
        for obstacle in obstacles:
            obstacle.update()

        remaining_obstacles = []
        for obstacle in obstacles:
            obstacle.draw(screen)

            if obstacle.x > 0:
                remaining_obstacles.append(obstacle)
        player.draw(screen)

        obstacles = remaining_obstacles
        if new_obstacle_delay > 0:
            new_obstacle_delay -= 1

        pygame.display.flip()
        clock.tick(30)

pygame.quit()