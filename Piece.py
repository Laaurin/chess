import os


class Piece:
    def __init__(self, color, image, pos, directions):
        self.image = os.path.join("Images", "Pieces", image)
        self.color = color
        self.pos = pos
        self.directions = directions
