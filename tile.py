import pygame

WHITE = (255, 255, 255)

class Tile:


    def __init__(self, left, top, width, height):
        self.surface = pygame.Surface((width, height))
        self.x = left
        self.y = top

    def update(self):
        pass
    
    def draw(self, surface):
        pygame.draw.rect(self.surface, WHITE, (0, 0, self.surface.get_width() - 1, self.surface.get_height() - 1))
        surface.blit(self.surface, (self.x, self.y))