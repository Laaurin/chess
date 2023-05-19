class Move:
    def __init__(self, start_square, destination_square, piece, captured_piece=None, rook_start_square=None,
                 rook_destination_square=None):
        self.start_square = start_square
        self.destination_square = destination_square
        self.piece = piece
        self.captured_piece = captured_piece
        self.rook_start_square = rook_start_square
        self.rook_destination_square = rook_destination_square

    def __str__(self):
        start_column = chr(ord('A') + self.start_square % 8)
        start_row = str(self.start_square // 8 + 1)
        destination_column = chr(ord('A') + self.destination_square % 8)
        destination_row = str(self.destination_square // 8 + 1)

        if self.captured_piece:
            return f"{start_column}{start_row} ({self.piece}) captured {destination_column}{destination_row} ({self.captured_piece})"
        return f"{start_column}{start_row} ({self.piece}) moved to {destination_column}{destination_row}"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.start_square == other.start_square and self.destination_square == other.destination_square:
                other.rook_start_square = self.rook_start_square
                other.rook_destination_square = self.rook_destination_square
                return True
            return False

        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
