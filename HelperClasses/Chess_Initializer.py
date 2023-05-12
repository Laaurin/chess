from Color import Color
from Pieces.Bishop import Bishop
from Pieces.King import King
from Pieces.Knight import Knight
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
from Pieces.Rook import Rook


class ChessInitializer:
    def __init__(self, FEN):
        self.board = [[None] * 8 for _ in range(8)]
        self.pieces = []
        self.load_from_FEN(FEN)

    def load_from_FEN(self, FEN):
        x = 0
        y = 0
        for sign in FEN:
            if sign == '/':
                x = 0
                y += 1

            elif sign.isnumeric():
                x += int(sign)

            else:
                self.add_piece(sign, x, y)
                x += 1

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
    def get_piece_from_char(self, piece, color, x, y):
        if piece == 'P':
            return Pawn(color, self.cords_to_index(x, y))

        if piece == 'R':
            return Rook(color, self.cords_to_index(x, y))

        if piece == 'K':
            return King(color, self.cords_to_index(x, y))

        if piece == 'N':
            return Knight(color, self.cords_to_index(x, y))

        if piece == 'Q':
            return Queen(color, self.cords_to_index(x, y))

        if piece == 'B':
            return Bishop(color, self.cords_to_index(x, y))

    def cords_to_index(self, x, y):
        index = 56 - y * 8 + (x % 8)
        return index
