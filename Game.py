import pygame

from Chess import Chess
from Visuals import Visuals


class Game:
    def __init__(self, FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"):
        self.chess = Chess(FEN)
        self.visuals = Visuals()

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

            pygame.display.update()