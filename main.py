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
game_over = False
score = 0

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
        screen.fill(SKY_BLUE)
        pygame.draw.rect(screen, SAND, (0, HEIGHT - 40, WIDTH, HEIGHT))

        if new_obstacle_delay == 0 and random.random() > 0.8:
            if random.choice(["rock", "cactus"]) == "rock":
                obstacles.append(Obstacle(WIDTH, 150, "rock.png", 5))
            else:
                obstacles.append(Obstacle(WIDTH, 130, "cactus.png", 10))
            new_obstacle_delay = 30

        if not game_over:
            player.update()
            for obstacle in obstacles:
                obstacle.update()

        remaining_obstacles = []
        for obstacle in obstacles:
            obstacle.draw(screen)

            if obstacle.x > 0:
                remaining_obstacles.append(obstacle)
            else:
                score += obstacle.score_value
                print("Scode:", score)

        player.draw(screen)

        obstacles = remaining_obstacles
        for obstacle in obstacles:
            if player.did_collide_with(obstacle.get_rect()):
                game_over = True
                print("Game Over")
                break

        if new_obstacle_delay > 0:
            new_obstacle_delay -= 1

        pygame.display.flip()
        clock.tick(30)

pygame.quit()