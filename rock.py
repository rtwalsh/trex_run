from tile import Tile

class Rock(Tile):

    def __init__(self, left, top):
        Tile.__init__(self, left, top, 20, 20)
        self.speed = 2

    def update(self):
        self.x -= self.speed
