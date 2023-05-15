import pygame
from HelperClasses import Calculation
from config import *


class Visuals:
    def __init__(self):
        pygame.init()
        self.tile_size = (min(WINDOW_HEIGHT, WINDOW_WIDTH) - 2 * max(OFFSET_VERTICAL, OFFSET_HORIZONTAL)) / 8
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
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
                                 (OFFSET_VERTICAL + j * self.tile_size,
                                  OFFSET_HORIZONTAL + i * self.tile_size,
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
        x, y = Calculation.get_square_cords_from_cords(pos)

        rect = pygame.Rect(x, y, self.tile_size, self.tile_size)
        surface = pygame.Surface((self.tile_size, self.tile_size), pygame.SRCALPHA)
        surface.fill((46, 204, 113, 128))
        self.screen.blit(surface, rect)

    def highlight_possible_capture(self, index):
        x, y = Calculation.index_to_pixel(index)
        pygame.draw.rect(self.screen, "blue",
                         (OFFSET_VERTICAL + x, OFFSET_HORIZONTAL + y,
                          self.tile_size, self.tile_size), 5)

    def highlight_possible_move(self, index):
        x, y = Calculation.index_to_pixel(index)
        pygame.draw.circle(self.screen, (46, 204, 113), (int(x + self.tile_size / 2), int(y + self.tile_size / 2)),
                           TILE_SIZE / 8)

    def display_piece(self, piece):
        picture = pygame.image.load(piece.image)
        picture = pygame.transform.scale(picture, (self.tile_size, self.tile_size))
        self.screen.blit(picture, Calculation.index_to_pixel(piece.pos))

    @staticmethod
    def print_board(board):
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
