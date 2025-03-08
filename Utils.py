import chess


def getMovesToTarget(board, start, target):
    start_squares = [chess.parse_square(start)]
    new_board = board.copy()
    for square in range(64):
        if square != chess.parse_square(target) and square != chess.parse_square(start) and new_board.piece_at(square) is None:
            piece = new_board.remove_piece_at(chess.parse_square(start))
            new_board.set_piece_at(square, piece)
            if new_board.is_legal(chess.Move.from_uci(chess.square_name(square) + target)):
                start_squares.append(square)
            new_board = board.copy()
    return start_squares


def getPossiblePieces(board, square):
    piece = board.piece_at(square)
    copy_board = board.copy()
    possiblePieces = [piece]
    if piece.symbol().lower() == 'b' or piece.symbol().lower() == 'r':
        newPiece = chess.Piece(5, chess.BLACK) if board.color_at(square) == chess.BLACK else chess.Piece(5, chess.WHITE)
        copy_board.set_piece_at(square, newPiece)
        if board.is_check() and copy_board.is_check() or not board.is_check() and not copy_board.is_check():
            possiblePieces.append(newPiece)
    return possiblePieces
