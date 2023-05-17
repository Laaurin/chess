import os
from HelperClasses import Calculation
from HelperClasses.Move import Move


class Piece:
    def __init__(self, color, image, pos, directions, is_sliding_piece):
        self.image = os.path.join("Images", "Pieces", image)
        self.color = color
        self.pos = pos
        self.directions = directions
        self.is_sliding_piece = is_sliding_piece

    def get_sliding_moves(self, board, current_turn):
        moves = []
        for direction in self.directions:
            for i in range(board.get_squares_to_edge(self.pos, direction)):
                x, y = Calculation.index_to_cords(self.pos + (i + 1) * direction)
                if board.board[y][x]:
                    if board.board[y][x].color == current_turn:
                        break

                    if board.board[y][x].color != current_turn:
                        moves.append(Move(self.pos, self.pos + (i + 1) * direction, board.board[y][x]))
                        break

                else:
                    moves.append(Move(self.pos, self.pos + (i + 1) * direction, None))

        return moves

    def get_non_sliding_moves(self, board, current_turn):
        moves = []
        for direction in self.directions:
            new_pos = self.pos + direction
            if not 0 <= new_pos <= 63:
                continue
            x, y = Calculation.index_to_cords(self.pos + direction)
            if board.board[y][x]:
                if board.board[y][x].color != current_turn:
                    moves.append(Move(self.pos, self.pos + direction, board.board[y][x]))
            else:
                moves.append(Move(self.pos, self.pos + direction, None))

        return moves

    def get_legal_moves(self, board, current_turn):
        pass
