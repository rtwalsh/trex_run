from tile import Tile

class Player(Tile):

    JUMP_AMOUNTS = [ 0, 36, 25, 16, 9, 5, 3, 2, 1, 0, 0, 0, -1. -2, -3, -5, -9, -16, -25, -36 ]

    def __init__(self, left, top):
        Tile.__init__(self, left, top, 50, 50)
        self.jumping = 0

    def jump(self):
        if self.jumping == 0:
            self.jumping = len(Player.JUMP_AMOUNTS) - 1

    def update(self):
        self.delta_y = Player.JUMP_AMOUNTS[self.jumping]
        self.y += self.delta_y
        if self.jumping > 0:
            self.jumping -= 1            
