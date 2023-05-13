from Piece import Piece
from Color import Color


class King(Piece):
    def __init__(self, color, pos):
        self.image = "king_black.png"
        if color == Color.WHITE:
            self.image = "king_white.png"
        super().__init__(color, self.image, pos, [-1, 7, 8, 9, 1, -7, -8, -9], False)

    def __str__(self):
        if self.color == Color.WHITE:
            return 'K'
        return 'k'
