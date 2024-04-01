import pygame

class Tile:


    def __init__(self, left, top, width, height):
        self.surface = pygame.Surface((width, height))
        self.x = left
        self.y = top

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.surface.get_width() - 1, self.surface.get_height() - 1)
    
    def update(self):
        pass
    
    def draw(self, surface):
        surface.blit(self.surface, (self.x, self.y))