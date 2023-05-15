import pygame

from HelperClasses import Calculation
from Chess import Chess
from Visuals import Visuals


class Game:
    def __init__(self, fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"):
        self.chess = Chess(fen)
        self.visuals = Visuals()

        self.available_moves = []
        self.selected_square = None
        self.selected_piece = None

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

                    if not Calculation.cords_inside_board(pos):
                        continue

                    # player clicked on square
                    self.handle_click(pos)

            pygame.display.update()

    def handle_click(self, pos):
        cord_x, cord_y = Calculation.pixel_to_cords(pos)

        if self.selected_piece:
            self.selected_square = Calculation.cords_to_index(cord_x, cord_y)

            if self.selected_square in self.available_moves:
                print("move successful!")
                self.chess.move(self.selected_piece.pos, self.selected_square)
                self.chess.switch_turn()

            print("piece deselected")
            self.available_moves = []
            self.selected_square = None
            self.selected_piece = None
            self.visuals.update(self.chess.pieces)

        else:
            print("trying to select piece")
            piece = self.chess.board.get_piece(cord_x, cord_y)

            if not piece:
                return

            elif piece.color != self.chess.current_turn:
                return

            else:
                print(f"selected piece ({piece})")
                self.selected_piece = piece
                self.visuals.highlight_square(self.selected_piece.pos)
                moves = self.chess.get_legal_moves(self.selected_piece)
                self.available_moves = [i.destination_square for i in moves]
                self.visuals.highlight_moves(moves)
