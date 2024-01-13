import pygame

class Tile:


    def __init__(self, left, top, width, height):
        self.surface = pygame.Surface((width, height))
        self.x = left
        self.y = top

    def update(self):
        pass
    
    def draw(self, surface):
        surface.blit(self.surface, (self.x, self.y))