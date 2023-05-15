from Color import Color
from HelperClasses.Chess_Initializer import ChessInitializer
from HelperClasses.Move import Move
from HelperClasses.Board import Board
from HelperClasses import Calculation
from Pieces.Pawn import Pawn


class Chess:
    def __init__(self, fen):
        self.initializer = ChessInitializer(fen)
        self.board = Board(self.initializer.board)
        self.pieces = self.initializer.pieces
        self.current_turn = self.initializer.current_turn
        self.K = self.initializer.K
        self.Q = self.initializer.Q
        self.k = self.initializer.k
        self.q = self.initializer.q

    def get_all_legal_moves(self):
        for piece in self.pieces:
            if piece.color != self.current_turn:
                continue
            self.get_legal_moves(piece)

    def get_legal_moves(self, piece):
        return piece.get_legal_moves(self.board, self.current_turn)

    def move(self, start_square, destination_square):
        x_start, y_start = Calculation.index_to_cords(start_square)
        x_destination, y_destination = Calculation.index_to_cords(destination_square)

        for piece in self.pieces:
            if piece.pos == destination_square:
                self.pieces.remove(piece)
                break
        self.board.board[y_destination][x_destination] = self.board.board[y_start][x_start]
        self.board.board[y_destination][x_destination].pos = destination_square

        self.board.board[y_start][x_start] = None

    def switch_turn(self):
        if self.current_turn == Color.WHITE:
            self.current_turn = Color.BLACK
        else:
            self.current_turn = Color.WHITE
