from Piece import Piece
from Color import Color


class Pawn(Piece):
    def __init__(self, color, pos):
        self.image = "felix.png"
        if color == Color.WHITE:
            self.image = "pawn_white.png"
        super().__init__(color, self.image, pos, [8, 16, 7, 9], False)

    def __str__(self):
        if self.color == Color.WHITE:
            return 'P'
        return 'p'


