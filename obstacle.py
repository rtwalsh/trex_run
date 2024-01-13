import pygame
from tile import Tile
from colors import *

class Obstacle(Tile):

    speed = 4

    def __init__(self, left, top, width, height):
        Tile.__init__(self, left, top, width, height)

    @classmethod
    def speed_up(cls):
        cls.speed += 1

    @classmethod
    def slow_down(cls):
        if cls.speed > 0:
            cls.speed -= 1
            
    def update(self):
        self.x -= Obstacle.speed

    def draw(self, screen):
        pygame.draw.rect(self.surface, WHITE, (0, 0, self.surface.get_width() - 1, self.surface.get_height() - 1))
        Tile.draw(self, screen)

