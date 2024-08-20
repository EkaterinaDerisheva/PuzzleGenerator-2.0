import chess

def getMovesToTarget(board, start, target):
    start_squares = []
    for square in chess.SQUARES:
        if square != target and not board.occupied(square):
            new_position = chess.square(square.file, start.rank)
            if board.is_legal(chess.Move(new_position, target)):
                start_squares += square
    return start_squares
