from HelperClasses import Calculation
from HelperClasses.Move import Move
from Piece import Piece
from Color import Color


class Pawn(Piece):
    def __init__(self, color, pos):
        image = "pawn_black.png"
        #image = "felix.png"

        directions = [-8]
        self.start_rank = 1

        if color == Color.WHITE:
            image = "pawn_white.png"
            directions = [8]
            self.start_rank = 6

        super().__init__(color, image, pos, directions, False)

    def get_legal_moves(self, board, current_turn):
        moves = []
        curr_rank, curr_file = 7 - self.pos // 8, self.pos % 8
        direction = self.directions[0]

        for offset in [-1, 1]:
            new_pos = self.pos + direction + offset
            x, y = Calculation.index_to_cords(new_pos)
            if 0 <= new_pos <= 63 and board.board[y][x] and board.board[y][x].color != current_turn:
                moves.append(Move(self.pos, new_pos, self, board.board[y][x]))

        new_pos = self.pos + direction

        x, y = Calculation.index_to_cords(new_pos)
        if not 0 <= new_pos <= 63 or board.board[y][x]:
            return moves  # no valid moves if pawn cannot move forward

        moves.append(Move(self.pos, new_pos, self))

        if curr_rank == self.start_rank:
            # check if pawn can move 2 squares forward
            new_pos = self.pos + 2 * direction
            x, y = Calculation.index_to_cords(new_pos)
            x2, y2 = Calculation.index_to_cords(self.pos + direction)
            if 0 <= new_pos <= 63 and not board.board[y][x] and not board.board[y2][x2]:
                moves.append(Move(self.pos, new_pos, self))

        # check for diagonal captures
        return moves

    def get_en_passant_move(self, last_move):
        en_passant_moves = []
        print(f"last move: {last_move}")

        # Überprüfen, ob der letzte Zug ein Doppelschritt eines gegnerischen Bauern war
        if isinstance(last_move.piece, Pawn) and abs(last_move.start_square - last_move.destination_square) == 16:
            print(abs(last_move.start_square - last_move.destination_square))
            # Überprüfen, ob der gegnerische Bauer neben diesem Bauern steht und auf der richtigen Reihe ist
            if abs(last_move.destination_square % 8 - self.pos % 8) == 1 and (
                    (self.color == Color.WHITE and self.pos // 8 == 4) or
                    (self.color == Color.BLACK and self.pos // 8 == 3)
            ):
                # Generiere den en passant Zug
                captured_piece = last_move.piece
                captured_piece_pos = last_move.destination_square
                en_passant_destination = captured_piece_pos + self.directions[0]

                # Erstelle das Move-Objekt für en passant
                move = Move(self.pos, en_passant_destination, self, captured_piece, captured_piece_pos, en_passant_destination)

                # Füge den en passant Zug zur Liste hinzu
                en_passant_moves.append(move)

        return en_passant_moves

    def __str__(self):
        if self.color == Color.WHITE:
            return 'P'
        return 'p'
