import pygame

from HelperClasses import Calculation
from Chess import Chess
from Visuals import Visuals


class Game:
    def __init__(self, fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"):
        self.chess = Chess(fen)
        self.visuals = Visuals()

        self.pos_1 = (-1, -1)
        self.pos_2 = (-1, -1)

    def run(self):
        available_moves = []
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
                    if not Calculation.cords_inside_board(pos):
                        continue
                    cord_x, cord_y = Calculation.pixel_to_cords(pos)
                    piece = self.chess.board.get_piece(cord_x, cord_y)

                    destination_square = Calculation.cords_to_index(cord_x, cord_y)
                    if destination_square in available_moves:
                        cord_x, cord_y = Calculation.pixel_to_cords(self.pos_1)
                        start_square = Calculation.cords_to_index(cord_x, cord_y)
                        self.chess.move(start_square, destination_square)
                        self.chess.switch_turn()
                        self.visuals.update(self.chess.pieces)
                        available_moves = []
                        self.pos_1 = (-1, -1)

                    elif not piece:
                        self.visuals.update(self.chess.pieces)
                        continue
                    elif piece.color != self.chess.current_turn:
                        continue

                    elif self.pos_1 == pos:
                        self.pos_1 = (-1, -1)
                        self.visuals.update(self.chess.pieces)

                    else:
                        self.visuals.update(self.chess.pieces)
                        self.pos_1 = pos
                        self.visuals.highlight_square(self.pos_1)
                        moves = self.chess.get_legal_moves(piece)
                        available_moves = [i.destination_square for i in moves]
                        self.visuals.highlight_moves(moves)

            pygame.display.update()
