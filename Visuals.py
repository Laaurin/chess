import pygame


class Visuals:
    def __init__(self):
        pygame.init()

        self.width = 800
        self.height = self.width
        self.offset_vertical = 0
        self.offset_horizontal = 0
        self.tile_size = (min(self.height, self.width) - 2 * max(self.offset_vertical, self.offset_horizontal)) / 8

        self.screen = pygame.display.set_mode((self.width, self.height))

        self.color_white = "#f0e2a3"
        self.color_black = "#084d17"

    def draw_board(self):
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    color = self.color_white
                else:
                    color = self.color_black
                pygame.draw.rect(self.screen, color,
                                 (self.offset_vertical + j * self.tile_size,
                                  self.offset_horizontal + i * self.tile_size,
                                  self.tile_size, self.tile_size))

    def draw_pieces(self, pieces):
        for piece in pieces:
            self.display_piece(piece)

    def display_piece(self, piece):
        picture = pygame.image.load(piece.image)
        picture = pygame.transform.scale(picture, (self.tile_size, self.tile_size))
        self.screen.blit(picture, self.index_to_pixel(piece.pos))

    def index_to_pixel(self, index):
        x = self.offset_vertical + (index % 8) * self.tile_size
        y = self.height - (int(index / 8) + 1) * self.tile_size

        return x, y
