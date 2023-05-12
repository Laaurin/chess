import pygame

from HelperClasses.Calculation import Calculation
from Chess import Chess
from Visuals import Visuals


class Game:
    def __init__(self, width=800, height=800, FEN="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"):
        self.calculation = Calculation(width, height, 0, 0)
        self.chess = Chess(FEN)
        self.visuals = Visuals(self.calculation)

        self.pos_1 = (-1, -1)
        self.pos_2 = (-1, -1)

    def run(self):
        self.visuals.draw_board()
        self.visuals.draw_pieces(self.chess.pieces)
        while True:
            # Behandle Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if not self.calculation.cords_inside_board(pos):
                        continue
                    if self.pos_1 == (-1, -1):
                        self.pos_1 = pos
                        self.visuals.highlight_square(self.pos_1)
                        cord_x, cord_y = self.calculation.pixel_to_cords(self.pos_1)
                        piece = self.chess.get_piece(cord_x, cord_y)
                        if piece:
                            moves = self.chess.get_legal_moves(piece)
                            self.visuals.highlight_moves(moves)

                    elif self.pos_1 == pos:
                        self.pos_1 = (-1, -1)
                        self.visuals.update(self.chess.pieces)

                    else:
                        self.pos_1 = (-1, -1)
                        self.visuals.update(self.chess.pieces)

            pygame.display.update()
