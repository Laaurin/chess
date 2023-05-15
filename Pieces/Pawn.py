from HelperClasses import Calculation
from HelperClasses.Move import Move
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

    def get_moves(self, board):
        moves = []
        curr_rank, curr_file = 7 - self.pos // 8, self.pos % 8
        direction = self.directions[0]

        for offset in [-1, 1]:
            new_pos = self.pos + direction + offset
            x, y = Calculation.index_to_cords(new_pos)
            if 0 <= new_pos <= 63 and board[y][x] and board[y][x].color != self.color:
                moves.append(Move(self.pos, new_pos, board[y][x]))

        new_pos = self.pos + direction

        x, y = Calculation.index_to_cords(new_pos)
        if not 0 <= new_pos <= 63 or board[y][x]:
            return moves  # no valid moves if pawn cannot move forward

        moves.append(Move(self.pos, new_pos))

        if curr_rank == self.start_rank:
            # check if pawn can move 2 squares forward
            new_pos = self.pos + 2 * direction
            x, y = Calculation.index_to_cords(new_pos)
            x2, y2 = Calculation.index_to_cords(self.pos + direction)
            if 0 <= new_pos <= 63 and not board[y][x] and not board[y2][x2]:
                moves.append(Move(self.pos, new_pos))

        # check for diagonal captures

        return moves

    def __str__(self):
        if self.color == Color.WHITE:
            return 'P'
        return 'p'
