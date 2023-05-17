from Piece import Piece
from Color import Color
from HelperClasses.Move import Move
from HelperClasses import Calculation


class Knight(Piece):
    def __init__(self, color, pos):
        self.image = "knight_black.png"
        if color == Color.WHITE:
            self.image = "knight_white.png"
        super().__init__(color, self.image, pos, [6, 15, 17, 10, -6, -15, -17, -10], False)

    def get_legal_moves(self, board, current_turn):
        moves = []
        for direction in self.directions:
            new_pos = self.pos + direction
            if not 0 <= new_pos <= 63:
                continue
            if direction % 8 > 2:
                if new_pos % 8 > self.pos % 8:
                    continue

            else:
                if new_pos % 8 < self.pos % 8:
                    continue
            x, y = Calculation.index_to_cords(self.pos + direction)
            if board.board[y][x]:
                if board.board[y][x].color != current_turn:
                    moves.append(Move(self.pos, self.pos + direction, board.board[y][x]))
            else:
                moves.append(Move(self.pos, self.pos + direction, None))

        return moves

    def __str__(self):
        if self.color == Color.WHITE:
            return 'N'
        return 'n'
