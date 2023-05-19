from Piece import Piece
from Color import Color
from HelperClasses import Calculation
from HelperClasses.Move import Move


class King(Piece):
    def __init__(self, color, pos):
        self.image = "king_black.png"
        #self.image = "marco_king.png"
        if color == Color.WHITE:
            self.image = "king_white.png"
            #self.image = "marco_king.png"

        super().__init__(color, self.image, pos, [-1, 7, 8, 9, 1, -7, -8, -9], False)

    def get_legal_moves(self, board, current_turn):
        return super().get_non_sliding_moves(board, current_turn)

    def castle_moves(self, board, king_side_castle, queen_side_castle):
        moves = []
        print(king_side_castle, queen_side_castle)
        cord_x, cord_y = Calculation.index_to_cords(self.pos)
        if king_side_castle:
            if not board.board[cord_y][cord_x + 1] and not board.board[cord_y][cord_x + 2]:
                moves.append(Move(self.pos, self.pos+2, self, None, self.pos+3, self.pos+1))

        if queen_side_castle:
            if not board.board[cord_y][cord_x - 1] and not board.board[cord_y][cord_x - 2]\
                    and not board.board[cord_y][cord_x - 2]:

                moves.append(Move(self.pos, self.pos-2, self, None, self.pos-4, self.pos-1))

        return moves

    def __str__(self):
        if self.color == Color.WHITE:
            return 'K'
        return 'k'
