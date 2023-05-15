from Piece import Piece
from Color import Color


class Knight(Piece):
    def __init__(self, color, pos):
        self.image = "knight_black.png"
        if color == Color.WHITE:
            self.image = "knight_white.png"
        super().__init__(color, self.image, pos, [6, 15, 17, 10, -6, -15, -17, -10], False)

    def get_legal_moves(self, board, current_turn):
        pass

    def __str__(self):
        if self.color == Color.WHITE:
            return 'N'
        return 'n'
