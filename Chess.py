from Color import Color
from HelperClasses.Chess_Initializer import ChessInitializer
from HelperClasses.Move import Move
from Pieces.Bishop import Bishop
from Pieces.King import King
from Pieces.Knight import Knight
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
from Pieces.Rook import Rook


class Chess:
    def __init__(self, FEN):
        self.initializer = ChessInitializer(FEN)
        self.board = self.initializer.board
        self.pieces = self.initializer.pieces
        self.current_turn = Color.WHITE

    def get_all_legal_moves(self):
        for piece in self.pieces:
            if piece.color != self.current_turn:
                continue
            self.get_legal_moves(piece)
    def get_legal_moves(self, piece):
        moves = []
        print(piece)
        if piece.is_sliding_piece:
            for direction in piece.directions:
                print(f"direction: {direction} | {self.get_squares_to_edge(piece.pos, direction)}")
                for i in range(self.get_squares_to_edge(piece.pos, direction)):
                    print(f"looking at {piece.pos + (i+1) * direction}")
                    x, y = self.index_to_cords(piece.pos + (i+1) * direction)
                    if self.board[y][x]:
                        if self.board[y][x].color == piece.color:
                            print("piece has the same color")
                            print(x, y)
                            print(self.board[y][x])
                            print(self.board[y][x].color, piece.color)

                            break

                        if self.board[y][x].color != piece.color:
                            moves.append(Move(piece.pos, piece.pos + (i+1) * direction, self.board[y][x]))
                            print("piece has different color. im gonna take it")
                            break



                    else:
                        moves.append(Move(piece.pos, piece.pos + (i+1) * direction, None))
                        print("no piece at this square")

        return moves

    def get_piece(self, x, y):
        return self.board[y][x]

    def get_squares_to_edge(self, position, direction):
        distance = 0

        if direction == 1 or direction == -1:
            return self.get_squares_horizontal(position, direction)

        if direction == 8 or direction == -8:
            return self.get_squares_vertical(position, direction)

        if direction == 7 or direction == -7 or direction == 9 or direction == -9:
            vertical = -8 if direction < 0 else 8
            horizontal = 1 if direction == 9 or direction == -7 else -1
            return min(self.get_squares_vertical(position, vertical), self.get_squares_horizontal(position, horizontal))

    def get_squares_vertical(self, position, direction):
        if not (direction == 8 or direction == -8):
            print("invalid direction")
            return
        squares = 0
        while 0 <= position + direction < 64:
            squares += 1
            position += direction

        return squares

    def get_squares_horizontal(self, position, direction):
        if not (direction == 1 or direction == -1):
            print("invalid direction")
            return

        squares = 0
        position %= 8
        while True:
            if position == 0 or position == 7:
                return squares
            squares += 1
            position += direction

    def index_to_cords(self, index):
        x = index % 8
        y = 7 - int(index / 8)
        return x, y

    def cords_to_index(self, x, y):
        index = 56 - y * 8 + (x % 8)
        return index