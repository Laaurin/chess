from Piece import Piece
from Color import Color


class Queen(Piece):
    def __init__(self, color, pos):
        self.image = "queen_black.png"
        if color == Color.WHITE:
            self.image = "queen_white.png"
        super().__init__(color, self.image, pos, [-1, 7, 8, 9, 1, -7, -8, -9], True)

    def get_legal_moves(self, board, current_turn):
        return super().get_sliding_moves(board, current_turn)

    def __str__(self):
        if self.color == Color.WHITE:
            return 'Q'
        return 'q'
