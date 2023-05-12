from Color import Color
from Pieces.Bishop import Bishop
from Pieces.King import King
from Pieces.Knight import Knight
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
from Pieces.Rook import Rook


class Chess:
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
                self.Add_Piece(sign, x, y)
                x += 1

    def Add_Piece(self, piece, x, y):
        color = Color.BLACK
        if piece.isupper():
            color = Color.WHITE
        piece = piece.upper()

        if piece == 'P':
            self.board[y][x] = Pawn(color, self.cords_to_index(x, y))

        elif piece == 'R':
            self.board[y][x] = Rook(color, self.cords_to_index(x, y))

        elif piece == 'K':
            self.board[y][x] = King(color, self.cords_to_index(x, y))

        elif piece == 'N':
            self.board[y][x] = Knight(color, self.cords_to_index(x, y))

        elif piece == 'Q':
            self.board[y][x] = Queen(color, self.cords_to_index(x, y))

        elif piece == 'B':
            self.board[y][x] = Bishop(color, self.cords_to_index(x, y))

        self.pieces.append(self.board[y][x])

    def cords_to_index(self, x, y):
        index = 56 - y * 8 + (x % 8)
        return index