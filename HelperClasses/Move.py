class Move:
    def __init__(self, start_square, destination_square, captured_piece):
        self.start_square = start_square
        self.destination_square = destination_square
        self.captured_piece = captured_piece

    def __str__(self):
        if self.captured_piece:
            return f"{self.start_square} -> {self.destination_square} ({self.captured_piece})"

        return f"{self.start_square} -> {self.destination_square}"
