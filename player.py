import pygame
from tile import Tile
from colors import *

class Player(Tile):

    JUMP_AMOUNTS = [ 0, 36, 25, 16, 9, 7, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, -1, -2, -3, -4, -5, -7, -9, -16, -25, -36 ]
    IMAGE_COUNT = 4

    def __init__(self, left, top):
        Tile.__init__(self, left, top, 50, 50)
        self.jumping = 0
        self.images = []
        for x in range(0, Player.IMAGE_COUNT):
            image = pygame.image.load(self.get_image_name(x))
            image.set_colorkey(image.get_at((0, 0)))
            self.images.append(image)
        self.image_index = 0

    def get_image_name(self, index):
        return "./assets/trex" + str(index + 1) + ".png"
    
    def jump(self):
        if self.jumping == 0:
            self.jumping = len(Player.JUMP_AMOUNTS) - 1

    def update(self):
        self.delta_y = Player.JUMP_AMOUNTS[self.jumping]
        self.y += self.delta_y
        if self.jumping > 0:
            self.jumping -= 1

        self.image_index = (self.image_index + 1) % len(self.images)

    def draw(self, screen):
        self.surface.fill(BLACK)
        self.surface.blit(self.images[self.image_index], (0, 0))
        Tile.draw(self, screen)

