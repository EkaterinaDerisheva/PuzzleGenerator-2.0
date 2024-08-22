import chess


def getMovesToTarget(board, start, target):
    start_squares = []
    for square in chess.SQUARES:
        if square != target and board.piece_at(square) is None:
            if board.is_legal(chess.Move(square, target)):
                start_squares += square
    return start_squares

