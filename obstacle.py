import pygame
from tile import Tile
from colors import *

class Obstacle(Tile):

    speed = 4

    @classmethod
    def speed_up(cls):
        cls.speed += 1

    @classmethod
    def slow_down(cls):
        if cls.speed > 0:
            cls.speed -= 1

    def __init__(self, left, top, image_name, score_value):
        self.image = pygame.image.load("./assets/" + image_name)
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.score_value = score_value + 2 * Obstacle.speed
        Tile.__init__(self, left, top, self.image.get_rect().width, self.image.get_rect().height)
            
    def update(self):
        self.x -= Obstacle.speed

    def draw(self, screen):
        self.surface.fill(BLACK)
        self.surface.set_colorkey(BLACK)
        self.surface.blit(self.image, (0, 0))
        Tile.draw(self, screen)

