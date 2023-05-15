from Piece import Piece
from Color import Color


class King(Piece):
    def __init__(self, color, pos):
        self.image = "king_black.png"
        self.image = "marco_king.png"
        if color == Color.WHITE:
            self.image = "king_white.png"
            self.image = "marco_king.png"

        super().__init__(color, self.image, pos, [-1, 7, 8, 9, 1, -7, -8, -9], False)

    def get_legal_moves(self, board, current_turn):
        return super().get_non_sliding_moves(board, current_turn)

    def __str__(self):
        if self.color == Color.WHITE:
            return 'K'
        return 'k'
