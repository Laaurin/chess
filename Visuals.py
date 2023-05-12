import pygame


class Visuals:
    def __init__(self, calculation):
        pygame.init()

        self.calculation = calculation
        self.width = 800
        self.height = self.width
        self.offset_vertical = 0
        self.offset_horizontal = 0
        self.tile_size = (min(self.height, self.width) - 2 * max(self.offset_vertical, self.offset_horizontal)) / 8

        self.screen = pygame.display.set_mode((self.width, self.height))

        self.color_white = "#f0e2a3"
        self.color_black = "#084d17"

    def update(self, pieces):
        self.draw_board()
        self.draw_pieces(pieces)
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

    def highlight_moves(self, moves):
        for move in moves:
            if move.captured_piece:
                self.highlight_possible_capture(move.destination_square)

            else:
                self.highlight_possible_move(move.destination_square)

    def highlight_square(self, pos):
        x, y = self.calculation.get_square_cords_from_cords(pos)

        rect = pygame.Rect(x, y, self.tile_size, self.tile_size)
        surface = pygame.Surface((self.tile_size, self.tile_size), pygame.SRCALPHA)
        surface.fill((46, 204, 113, 128))
        self.screen.blit(surface, rect)
    def highlight_possible_capture(self, index):
        x, y = self.index_to_pixel(index)
        pygame.draw.rect(self.screen, "blue",
                         (self.offset_vertical + x, self.offset_horizontal + y,
                          self.tile_size, self.tile_size), 5)

    def highlight_possible_move(self, index):
        x, y = self.index_to_pixel(index)
        pygame.draw.circle(self.screen, "blue", (int(x + self.calculation.tile_size / 2), int(y + self.calculation.tile_size / 2)),
                           self.calculation.tile_size / 8)
    def display_piece(self, piece):
        picture = pygame.image.load(piece.image)
        picture = pygame.transform.scale(picture, (self.tile_size, self.tile_size))
        self.screen.blit(picture, self.index_to_pixel(piece.pos))

    def index_to_pixel(self, index):
        x = self.offset_vertical + (index % 8) * self.tile_size
        y = self.height - (int(index / 8) + 1) * self.tile_size

        return x, y

    def pixel_to_cords(self, x, y):
        row = int((y - self.offset_vertical) / 8)
        col = int((x - self.offset_vertical) % 8)

    def print_board(self, board):
        for i in range(8):
            line = ""
            for j in range(8):
                value = board[i][j]
                if not board[i][j]:
                    value = ' '
                if (i + j) % 2 == 0:
                    line += f" {value} "
                else:
                    line += f"[{value}]"
            print(line)
