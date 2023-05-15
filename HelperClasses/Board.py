class Board:
    def __init__(self, board):
        self.board = board

    def get_squares_to_edge(self, position, direction):
        if direction == 1 or direction == -1:
            return self.get_squares_horizontal(position, direction)

        if direction == 8 or direction == -8:
            return self.get_squares_vertical(position, direction)

        if direction == 7 or direction == -7 or direction == 9 or direction == -9:
            vertical = -8 if direction < 0 else 8
            horizontal = 1 if direction == 9 or direction == -7 else -1
            return min(self.get_squares_vertical(position, vertical), self.get_squares_horizontal(position, horizontal))

    def get_squares_vertical(self, position, direction):
        squares = 0
        while 0 <= position + direction < 64:
            squares += 1
            position += direction

        return squares

    def get_squares_horizontal(self, position, direction):
        squares = 0
        position %= 8
        while True:
            if (position == 0 and direction == -1) or (position == 7 and direction == 1):
                return squares
            squares += 1
            position += direction

    def get_piece(self, x, y):
        return self.board[y][x]
