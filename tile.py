import pygame

WHITE = (255, 255, 255)

class Tile:

    JUMP_AMOUNTS = [ 0, 36, 25, 16, 9, 5, 3, 2, 1, 0, 0, 0, -1. -2, -3, -5, -9, -16, -25, -36 ]

    def __init__(self, left, top, width, height):
        self.surface = pygame.Surface((width, height))
        self.x = left
        self.y = top
        self.jumping = 0

    def jump(self):
        if self.jumping == 0:
            self.jumping = len(Tile.JUMP_AMOUNTS) - 1

    def update(self):
        self.delta_y = Tile.JUMP_AMOUNTS[self.jumping]
        self.y += self.delta_y
        if self.jumping > 0:
            self.jumping -= 1            

    def draw(self, surface):
        pygame.draw.rect(self.surface, WHITE, (0, 0, self.surface.get_width() - 1, self.surface.get_height() - 1))
        surface.blit(self.surface, (self.x, self.y))