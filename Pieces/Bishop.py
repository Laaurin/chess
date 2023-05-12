from Piece import Piece
from Color import Color


class Bishop(Piece):
    def __init__(self, color, pos):
        self.image = "bishop_black.png"
        if color == Color.WHITE:
            self.image = "bishop_white.png"
        super().__init__(color, self.image, pos, [7, 9, -7, -9], True)

    def __str__(self):
        if self.color == Color.WHITE:
            return 'B'
        return 'b'
