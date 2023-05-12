from Piece import Piece
from Color import Color


class King(Piece):
    def __init__(self, color, pos):
        self.image = "erik_king.png"
        if color == Color.WHITE:
            self.image = "marco_king.png"
        super().__init__(color, self.image, pos, [-1, 7, 8, 9, 1, -7, -8, -9])

    def __str__(self):
        if self.color == Color.WHITE:
            return 'K'
        return 'k'
