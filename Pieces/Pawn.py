from Piece import Piece
from Color import Color


class Pawn(Piece):
    def __init__(self, color, pos):
        image = "pawn_black.png"
        directions = [-8]
        self.start_rank = 1

        if color == Color.WHITE:
            image = "pawn_white.png"
            directions = [8]
            self.start_rank = 6


        super().__init__(color, image, pos, directions, False)

    def __str__(self):
        if self.color == Color.WHITE:
            return 'P'
        return 'p'


