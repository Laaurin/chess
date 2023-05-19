import pygame

from HelperClasses import Calculation
from HelperClasses.Move import Move
from Chess import Chess
from Visuals import Visuals


class Game:
    def __init__(self, fen="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        self.chess = Chess(fen)
        self.visuals = Visuals()

        self.available_moves = []
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
            selected_square = Calculation.cords_to_index(cord_x, cord_y)
            proposed_move = Move(self.selected_piece.pos, selected_square, self.selected_piece)

            if proposed_move in self.available_moves:
                print(proposed_move)
                self.chess.move(proposed_move)
                self.chess.stored_moves.append(proposed_move)

                self.chess.switch_turn()

            self.available_moves = []
            self.selected_piece = None
            self.visuals.update(self.chess.pieces)

        else:
            piece = self.chess.board.get_piece(cord_x, cord_y)

            if not piece:
                return

            elif piece.color != self.chess.current_turn:
                return

            else:
                self.selected_piece = piece
                self.visuals.highlight_square(self.selected_piece.pos)
                self.available_moves = self.chess.get_legal_moves(self.selected_piece)
                self.visuals.highlight_moves(self.available_moves)
