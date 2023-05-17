from Piece import Piece
from Color import Color


class Rook(Piece):
    def __init__(self, color, pos):
        self.image = "rook_black.png"
        if color == Color.WHITE:
            self.image = "rook_white.png"
        super().__init__(color, self.image, pos, [-1, 8, 1, -8], True)

    def get_legal_moves(self, board, current_turn):
        return super().get_sliding_moves(board, current_turn)

    def __str__(self):
        if self.color == Color.WHITE:
            return 'R'
        return 'r'
