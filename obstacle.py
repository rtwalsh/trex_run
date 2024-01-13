from tile import Tile

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
