from HelperClasses import Calculation
from Color import Color
from Pieces.Bishop import Bishop
from Pieces.King import King
from Pieces.Knight import Knight
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
from Pieces.Rook import Rook


class ChessInitializer:
    def __init__(self, fen):
        self.board = [[None] * 8 for _ in range(8)]
        self.pieces = []
        self.load_from_FEN(fen)
        self.current_turn = Color.WHITE
        self.K = False
        self.Q = False
        self.k = False
        self.q = False

    def load_from_FEN(self, fen):
        x = 0
        y = 0
        fen = fen.split(' ')
        for sign in fen[0]:
            if sign == '/':
                x = 0
                y += 1

            elif sign.isnumeric():
                x += int(sign)

            else:
                self.add_piece(sign, x, y)
                x += 1

        if fen[1] == 'b':
            self.current_turn = Color.BLACK

        for i in fen[2]:
            if i == 'K':
                self.K = True

            elif i == 'Q':
                self.Q = True

            elif i == 'k':
                self.k = True

            elif i == 'q':
                self.q = True

    def add_piece(self, piece_char, x, y):
        color = self.get_color_from_char(piece_char)

        piece_char = piece_char.upper()

        piece = self.get_piece_from_char(piece_char, color, x, y)

        self.board[y][x] = piece
        self.pieces.append(piece)

    def get_color_from_char(self, piece_char):
        color = Color.BLACK
        if piece_char.isupper():
            color = Color.WHITE
        return color

    @staticmethod
    def get_piece_from_char(piece, color, x, y):
        if piece == 'P':
            return Pawn(color, Calculation.cords_to_index(x, y))

        if piece == 'R':
            return Rook(color, Calculation.cords_to_index(x, y))

        if piece == 'K':
            return King(color, Calculation.cords_to_index(x, y))

        if piece == 'N':
            return Knight(color, Calculation.cords_to_index(x, y))

        if piece == 'Q':
            return Queen(color, Calculation.cords_to_index(x, y))

        if piece == 'B':
            return Bishop(color, Calculation.cords_to_index(x, y))


