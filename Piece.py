import os


class Piece:
    def __init__(self, color, image, pos, directions, is_sliding_piece):
        self.image = os.path.join("Images", "Pieces", image)
        self.color = color
        self.pos = pos
        self.directions = directions
        self.is_sliding_piece = is_sliding_piece