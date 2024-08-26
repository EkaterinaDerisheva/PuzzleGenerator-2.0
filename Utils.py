import chess


def getMovesToTarget(board, start, target):
    start_squares = []
    new_board = board.copy()
    for square in range(64):
        if square != chess.parse_square(target) and square != chess.parse_square(start) and new_board.piece_at(square) is None:
            piece = new_board.remove_piece_at(chess.parse_square(start))
            new_board.set_piece_at(square, piece)
            if new_board.is_legal(chess.Move.from_uci(chess.square_name(square) + target)):
                start_squares.append(square)
            new_board = board.copy()
    return start_squares

