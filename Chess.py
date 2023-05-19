from Color import Color
from HelperClasses.Chess_Initializer import ChessInitializer
from HelperClasses.Move import Move
from HelperClasses.Board import Board
from HelperClasses import Calculation
from Pieces.Pawn import Pawn
from Pieces.King import King
from Pieces.Rook import Rook


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

        self.stored_moves = []

    def get_all_legal_moves(self):
        for piece in self.pieces:
            if piece.color != self.current_turn:
                continue
            self.get_legal_moves(piece)

    def get_legal_moves(self, piece):
        moves = piece.get_legal_moves(self.board, self.current_turn)
        if piece.__class__ == King:
            if piece.color == Color.WHITE:
                moves.extend(piece.castle_moves(self.board, self.K, self.Q))
            else:
                moves.extend(piece.castle_moves(self.board, self.k, self.q))

        elif piece.__class__ == Pawn and self.stored_moves:
            print("checking for en passant")
            moves.extend(piece.get_en_passant_move(self.stored_moves[-1]))

        return moves

    def move(self, move):
        x_start, y_start = Calculation.index_to_cords(move.start_square)
        x_destination, y_destination = Calculation.index_to_cords(move.destination_square)

        # remove captured piece from piece list
        for piece in self.pieces:
            if piece.pos == move.destination_square:
                if piece.__class__ == Rook:
                    pass
                    # block rook from castling

                self.pieces.remove(piece)
                break

        # check if castling is still allowed

        self.handle_castle_rights(move.piece, x_start, y_start)

        self.board.board[y_destination][x_destination] = self.board.board[y_start][x_start]
        self.board.board[y_destination][x_destination].pos = move.destination_square

        if move.rook_start_square:
            x_start_rook, y_start_rook = Calculation.index_to_cords(move.rook_start_square)
            x_destination_rook, y_destination_rook = Calculation.index_to_cords(move.rook_destination_square)
            self.board.board[y_destination_rook][x_destination_rook] = self.board.board[y_start_rook][x_start_rook]
            self.board.board[y_destination_rook][x_destination_rook].pos = move.rook_destination_square

        self.board.board[y_start][x_start] = None

    def switch_turn(self):
        if self.current_turn == Color.WHITE:
            self.current_turn = Color.BLACK
        else:
            self.current_turn = Color.WHITE

    def handle_castle_rights(self, piece, x_start, y_start):
        if piece.__class__ == King:
            if piece.color == Color.WHITE:
                self.K = False
                self.Q = False
            else:
                self.k = False
                self.q = False

        if piece.__class__ == Rook:
            if (x_start, y_start) == (0, 0):
                self.q = False
            elif (x_start, y_start) == (0, 7):
                self.k = False
            elif (x_start, y_start) == (7, 0):
                self.Q = False
            elif (x_start, y_start) == (7, 7):
                self.K = False
