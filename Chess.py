from Color import Color
from HelperClasses.Chess_Initializer import ChessInitializer
from HelperClasses.Move import Move
from Pieces.Pawn import Pawn


class Chess:
    def __init__(self, FEN):
        self.initializer = ChessInitializer(FEN)
        self.board = self.initializer.board
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
        if piece.is_sliding_piece:
            moves = self.get_sliding_moves(piece)

        elif piece.__class__ == Pawn:
            moves = self.get_pawn_moves(piece)

        else:
            moves = self.get_non_sliding_moves(piece)
        return moves

    def get_sliding_moves(self, piece):
        moves = []
        for direction in piece.directions:
            for i in range(self.get_squares_to_edge(piece.pos, direction)):
                x, y = self.index_to_cords(piece.pos + (i + 1) * direction)
                if self.board[y][x]:
                    if self.board[y][x].color == self.current_turn:
                        break

                    if self.board[y][x].color != self.current_turn:
                        moves.append(Move(piece.pos, piece.pos + (i + 1) * direction, self.board[y][x]))
                        break

                else:
                    moves.append(Move(piece.pos, piece.pos + (i + 1) * direction, None))

        return moves

    def get_non_sliding_moves(self, piece):
        moves = []
        for direction in piece.directions:
            new_pos = piece.pos + direction
            if not 0 <= new_pos <= 63:
                continue
            x, y = self.index_to_cords(piece.pos + direction)
            if self.board[y][x]:
                if self.board[y][x].color != self.current_turn:
                    moves.append(Move(piece.pos, piece.pos + direction, self.board[y][x]))
            else:
                moves.append(Move(piece.pos, piece.pos + direction, None))

        return moves

    def get_pawn_moves(self, pawn):
        moves = []
        curr_rank, curr_file = 7 - pawn.pos // 8, pawn.pos % 8
        direction = pawn.directions[0]

        for offset in [-1, 1]:
            new_pos = pawn.pos + direction + offset
            x, y = self.index_to_cords(new_pos)
            if 0 <= new_pos <= 63 and self.board[y][x] and self.board[y][x].color != self.current_turn:
                moves.append(Move(pawn.pos, new_pos, self.board[y][x]))

        new_pos = pawn.pos + direction

        x, y = self.index_to_cords(new_pos)
        if not 0 <= new_pos <= 63 or self.board[y][x]:
            return moves  # no valid moves if pawn cannot move forward

        moves.append(Move(pawn.pos, new_pos))

        if curr_rank == pawn.start_rank:
            # check if pawn can move 2 squares forward
            new_pos = pawn.pos + 2 * direction
            x, y = self.index_to_cords(new_pos)
            x2, y2 = self.index_to_cords(pawn.pos + direction)
            if 0 <= new_pos <= 63 and not self.board[y][x] and not self.board[y2][x2]:
                moves.append(Move(pawn.pos, new_pos))

        # check for diagonal captures

        return moves

    def get_piece(self, x, y):
        return self.board[y][x]

    def move(self, start_square, destination_square):
        x_start, y_start = self.index_to_cords(start_square)
        print(x_start, y_start)
        x_destination, y_destination = self.index_to_cords(destination_square)

        for piece in self.pieces:
            if piece.pos == destination_square:
                self.pieces.remove(piece)
                break
        self.board[y_destination][x_destination] = self.board[y_start][x_start]
        self.board[y_destination][x_destination].pos = destination_square

        self.board[y_start][x_start] = None

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
            if (position == 0 and direction == -1) or (position == 7 and direction == 1):
                return squares
            squares += 1
            position += direction

    def switch_turn(self):
        if self.current_turn == Color.WHITE:
            self.current_turn = Color.BLACK
        else:
            self.current_turn = Color.WHITE

    def index_to_cords(self, index):
        x = index % 8
        y = 7 - int(index / 8)
        return x, y

    def cords_to_index(self, x, y):
        index = 56 - y * 8 + (x % 8)
        return index
