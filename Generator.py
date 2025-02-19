
import chess
import pandas as pd

import Utils
import PuzzleManager


def generateMateIn2(puzzleOrig):
    df = pd.DataFrame(columns=['generatedID', 'FEN', 'MoveSet', 'Level'])
    # df = pd.DataFrame()
    origId = puzzleOrig[0]
    origFen = puzzleOrig[1]
    origMoveSet = puzzleOrig[2].split()
    origLevel = puzzleOrig[10]
    origBoard = chess.Board(origFen)
    indexPos1 = 0

    # генерация первого хода игрока
    board = origBoard.copy()
    board0 = board.copy()
    board0.push(chess.Move.from_uci('0000'))
    humanPoses1 = Utils.getMovesToTarget(board0, origMoveSet[1][0:2], origMoveSet[1][2:4])
    if chess.parse_square(origMoveSet[0][2:4]) in humanPoses1:
        humanPoses1.remove(chess.parse_square(origMoveSet[0][2:4]))
    for humanPose in humanPoses1[:]:
        moveSet = list(origMoveSet)
        piece = board.remove_piece_at(chess.parse_square(moveSet[1][0:2]))
        board.set_piece_at(humanPose, piece)
        if not board.is_legal(chess.Move.from_uci(moveSet[0])) or board.is_variant_end() or board.gives_check(chess.Move.from_uci(moveSet[0])):
            humanPoses1.remove(humanPose)
    for humanPose1 in humanPoses1:
        indexPos1 += 1
        indexPiece1 = 0
        moveSet = list(origMoveSet)
        board = origBoard.copy()
        piece = board.remove_piece_at(chess.parse_square(moveSet[1][0:2]))
        board.set_piece_at(humanPose1, piece)
        moveSet[1] = chess.square_name(humanPose1) + moveSet[1][2:4]
        possiblePieces1 = Utils.getPossiblePieces(board, chess.parse_square(moveSet[1][0:2]))
        for humanPiece in possiblePieces1[:]:
            board1 = board.copy()
            board1.set_piece_at(humanPose1, humanPiece)
            board1.push(chess.Move.from_uci(moveSet[0]))
            if board1.is_variant_end():
                possiblePieces1.remove(humanPiece)
                continue
        for humanPiece in possiblePieces1:
            indexPiece1 += 1
            indexPos2 = 0
            board.set_piece_at(humanPose1, humanPiece)

            # генерация второго хода игрока
            if origMoveSet[1][2:4] != origMoveSet[3][0:2]:
                board0 = board.copy()
                board0.push(chess.Move.from_uci('0000'))
                humanPoses2 = Utils.getMovesToTarget(board0, moveSet[3][0:2], moveSet[3][2:4])
                if chess.parse_square(moveSet[0][2:4]) in humanPoses2:
                    humanPoses2.remove(chess.parse_square(moveSet[0][2:4]))
                if chess.parse_square(moveSet[1][2:4]) in humanPoses2:
                    humanPoses2.remove(chess.parse_square(moveSet[1][2:4]))
                if chess.parse_square(moveSet[2][2:4]) in humanPoses2:
                    humanPoses2.remove(chess.parse_square(moveSet[2][2:4]))
                for humanPose2 in humanPoses2[:]:
                    board2 = board.copy()
                    piece = board2.remove_piece_at(chess.parse_square(moveSet[3][0:2]))
                    board2.set_piece_at(humanPose2, piece)
                    if board2.is_variant_end():
                        humanPoses2.remove(humanPose2)
                        continue
                    if not board2.is_legal(chess.Move.from_uci(moveSet[0])):
                        humanPoses2.remove(humanPose2)
                        continue
                    board2.push(chess.Move.from_uci(moveSet[0]))
                    if board2.is_variant_end():
                        humanPoses2.remove(humanPose2)
                        continue
                    if not board2.is_legal(chess.Move.from_uci(moveSet[1])):
                        humanPoses2.remove(humanPose2)
                        continue
                    board2.push(chess.Move.from_uci(moveSet[1]))
                    if board2.is_variant_end():
                        humanPoses2.remove(humanPose2)
                        continue
                    if not board2.is_legal(chess.Move.from_uci(moveSet[2])):
                        humanPoses2.remove(humanPose2)
                        continue
                    board2.push(chess.Move.from_uci(moveSet[2]))
                    if board2.is_variant_end():
                        humanPoses2.remove(humanPose2)
                        continue
                    if board2.is_check():
                        humanPoses2.remove(humanPose2)
                        continue
                    if not board2.is_legal(chess.Move.from_uci(chess.square_name(humanPose2) + moveSet[3][2:4])):
                        humanPoses2.remove(humanPose2)
                        continue
                    board2.push(chess.Move.from_uci(chess.square_name(humanPose2) + moveSet[3][2:4]))
                    if board2.is_variant_end():
                        humanPoses2.remove(humanPose2)
                        continue
                    if not board2.is_check():
                        humanPoses2.remove(humanPose2)
                        continue
                for humanPose2 in humanPoses2:
                    indexPos2 += 1
                    piece = board.remove_piece_at(chess.parse_square(moveSet[3][0:2]))
                    board.set_piece_at(humanPose2, piece)
                    moveSet[3] = chess.square_name(humanPose2) + moveSet[3][2:4]

                    newMoveSet = " ".join(moveSet)
                    puzzleID = str(origId) + '_' + str(indexPos1) + '_' + str(indexPiece1) + '_' + str(indexPos2)
                    newPuzzle = [puzzleID, board.fen(), newMoveSet, origLevel]
                    df = pd.concat([df, pd.DataFrame([newPuzzle], columns=['generatedID', 'FEN', 'MoveSet', 'Level'])])
                    print(newPuzzle)
            else:
                newMoveSet = " ".join(moveSet)
                puzzleID = str(origId) + '_' + str(indexPos1) + '_' + str(indexPiece1) + '_' + str(indexPos2)
                newPuzzle = [puzzleID, board.fen(), newMoveSet, origLevel]
                df = pd.concat([df, pd.DataFrame([newPuzzle], columns=['generatedID', 'FEN', 'MoveSet', 'Level'])])
                print(newPuzzle)
    return df


def generateMateIn3(puzzleOrig):
    df = pd.DataFrame(columns=['generatedID', 'FEN', 'MoveSet', 'Level'])
    origId = puzzleOrig[0]
    origFen = puzzleOrig[1]
    origMoveSet = puzzleOrig[2].split()
    origLevel = puzzleOrig[10]
    origBoard = chess.Board(origFen)
    indexPos1 = 0

    # генерация первого хода игрока
    board = origBoard.copy()
    board0 = board.copy()
    board0.push(chess.Move.from_uci('0000'))
    humanPoses1 = Utils.getMovesToTarget(board0, origMoveSet[1][0:2], origMoveSet[1][2:4])
    if chess.parse_square(origMoveSet[0][2:4]) in humanPoses1:
        humanPoses1.remove(chess.parse_square(origMoveSet[0][2:4]))
    for humanPose in humanPoses1[:]:
        moveSet = list(origMoveSet)
        piece = board.remove_piece_at(chess.parse_square(moveSet[1][0:2]))
        board.set_piece_at(humanPose, piece)
        if not board.is_legal(chess.Move.from_uci(moveSet[0])) or board.is_variant_end() or board.gives_check(chess.Move.from_uci(moveSet[0])):
            humanPoses1.remove(humanPose)
    for humanPose1 in humanPoses1:
        indexPos1 += 1
        indexPiece1 = 0
        moveSet = list(origMoveSet)
        board = origBoard.copy()
        piece = board.remove_piece_at(chess.parse_square(moveSet[1][0:2]))
        board.set_piece_at(humanPose1, piece)
        moveSet[1] = chess.square_name(humanPose1) + moveSet[1][2:4]
        possiblePieces1 = Utils.getPossiblePieces(board, chess.parse_square(moveSet[1][0:2]))
        for humanPiece in possiblePieces1[:]:
            board1 = board.copy()
            board1.set_piece_at(humanPose1, humanPiece)
            board1.push(chess.Move.from_uci(moveSet[0]))
            if board1.is_variant_end():
                possiblePieces1.remove(humanPiece)
                continue
        for humanPiece in possiblePieces1:
            indexPiece1 += 1
            indexPos2 = 0
            indexPos3 = 0
            board.set_piece_at(humanPose1, humanPiece)

            # генерация второго хода игрока
            if origMoveSet[1][2:4] != origMoveSet[3][0:2]:
                board0 = board.copy()
                board0.push(chess.Move.from_uci('0000'))
                humanPoses2 = Utils.getMovesToTarget(board0, moveSet[3][0:2], moveSet[3][2:4])
                if chess.parse_square(moveSet[0][2:4]) in humanPoses2:
                    humanPoses2.remove(chess.parse_square(moveSet[0][2:4]))
                if chess.parse_square(moveSet[1][2:4]) in humanPoses2:
                    humanPoses2.remove(chess.parse_square(moveSet[1][2:4]))
                if chess.parse_square(moveSet[2][2:4]) in humanPoses2:
                    humanPoses2.remove(chess.parse_square(moveSet[2][2:4]))
                for humanPose2 in humanPoses2[:]:
                    board2 = board.copy()
                    piece = board2.remove_piece_at(chess.parse_square(moveSet[3][0:2]))
                    board2.set_piece_at(humanPose2, piece)
                    if board2.is_variant_end():
                        humanPoses2.remove(humanPose2)
                        continue
                    if not board2.is_legal(chess.Move.from_uci(moveSet[0])):
                        humanPoses2.remove(humanPose2)
                        continue
                    board2.push(chess.Move.from_uci(moveSet[0]))
                    if board2.is_variant_end():
                        humanPoses2.remove(humanPose2)
                        continue
                    if not board2.is_legal(chess.Move.from_uci(moveSet[1])):
                        humanPoses2.remove(humanPose2)
                        continue
                    board2.push(chess.Move.from_uci(moveSet[1]))
                    if board2.is_variant_end():
                        humanPoses2.remove(humanPose2)
                        continue
                    if not board2.is_legal(chess.Move.from_uci(moveSet[2])):
                        humanPoses2.remove(humanPose2)
                        continue
                    board2.push(chess.Move.from_uci(moveSet[2]))
                    if board2.is_variant_end():
                        humanPoses2.remove(humanPose2)
                        continue
                    if board2.is_check():
                        humanPoses2.remove(humanPose2)
                        continue
                    if not board2.is_legal(chess.Move.from_uci(chess.square_name(humanPose2) + moveSet[3][2:4])):
                        humanPoses2.remove(humanPose2)
                        continue
                    board2.push(chess.Move.from_uci(chess.square_name(humanPose2) + moveSet[3][2:4]))
                    if board2.is_variant_end():
                        humanPoses2.remove(humanPose2)
                        continue
                for humanPose2 in humanPoses2:
                    indexPos2 += 1
                    indexPos3 = 0
                    piece = board.remove_piece_at(chess.parse_square(moveSet[3][0:2]))
                    board.set_piece_at(humanPose2, piece)
                    moveSet[3] = chess.square_name(humanPose2) + moveSet[3][2:4]

                    #генерация третьего хода
                    if origMoveSet[5][0:2] != origMoveSet[3][2:4] and origMoveSet[5][0:2] != origMoveSet[1][2:4]:
                        board0 = board.copy()
                        board0.push(chess.Move.from_uci('0000'))
                        humanPoses3 = Utils.getMovesToTarget(board0, moveSet[5][0:2], moveSet[5][2:4])
                        if chess.parse_square(moveSet[0][2:4]) in humanPoses2:
                            humanPoses2.remove(chess.parse_square(moveSet[0][2:4]))
                        if chess.parse_square(moveSet[1][2:4]) in humanPoses2:
                            humanPoses2.remove(chess.parse_square(moveSet[1][2:4]))
                        if chess.parse_square(moveSet[2][2:4]) in humanPoses2:
                            humanPoses2.remove(chess.parse_square(moveSet[2][2:4]))
                        if chess.parse_square(moveSet[3][2:4]) in humanPoses2:
                            humanPoses2.remove(chess.parse_square(moveSet[3][2:4]))
                        if chess.parse_square(moveSet[4][2:4]) in humanPoses2:
                            humanPoses2.remove(chess.parse_square(moveSet[4][2:4]))
                        for humanPose3 in humanPoses3[:]:
                            board3 = board.copy()
                            piece = board3.remove_piece_at(chess.parse_square(moveSet[5][0:2]))
                            board3.set_piece_at(humanPose3, piece)
                            if board3.is_variant_end():
                                humanPoses3.remove(humanPose3)
                                continue
                            if not board3.is_legal(chess.Move.from_uci(moveSet[0])):
                                humanPoses3.remove(humanPose3)
                                continue
                            board3.push(chess.Move.from_uci(moveSet[0]))
                            if board3.is_variant_end():
                                humanPoses3.remove(humanPose3)
                                continue
                            if not board3.is_legal(chess.Move.from_uci(moveSet[1])):
                                humanPoses3.remove(humanPose3)
                                continue
                            board3.push(chess.Move.from_uci(moveSet[1]))
                            if board3.is_variant_end():
                                humanPoses3.remove(humanPose3)
                                continue
                            if not board3.is_legal(chess.Move.from_uci(moveSet[2])):
                                humanPoses3.remove(humanPose3)
                                continue
                            board3.push(chess.Move.from_uci(moveSet[2]))
                            if board3.is_variant_end():
                                humanPoses3.remove(humanPose3)
                                continue
                            if board3.is_check():
                                humanPoses3.remove(humanPose3)
                                continue
                            if not board3.is_legal(chess.Move.from_uci(moveSet[3])):
                                humanPoses3.remove(humanPose3)
                                continue
                            board3.push(chess.Move.from_uci(moveSet[3]))
                            if board3.is_variant_end():
                                humanPoses3.remove(humanPose3)
                                continue
                            if not board3.is_legal(chess.Move.from_uci(moveSet[4])):
                                humanPoses3.remove(humanPose3)
                                continue
                            board3.push(chess.Move.from_uci(moveSet[4]))
                            if board3.is_variant_end():
                                humanPoses3.remove(humanPose3)
                                continue
                            if board3.is_check():
                                humanPoses3.remove(humanPose3)
                                continue
                            if not board3.is_legal(chess.Move.from_uci(chess.square_name(humanPose3) + moveSet[5][2:4])):
                                humanPoses3.remove(humanPose3)
                                continue
                            board3.push(chess.Move.from_uci(chess.square_name(humanPose3) + moveSet[5][2:4]))
                            if board3.is_variant_end():
                                humanPoses3.remove(humanPose3)
                                continue
                            if not board3.is_check():
                                humanPoses3.remove(humanPose3)
                                continue
                        for humanPose3 in humanPoses3:
                            indexPos3 += 1
                            piece = board.remove_piece_at(chess.parse_square(moveSet[5][0:2]))
                            board.set_piece_at(humanPose3, piece)
                            moveSet[5] = chess.square_name(humanPose3) + moveSet[5][2:4]

                            newMoveSet = " ".join(moveSet)
                            puzzleID = str(origId) + '_' + str(indexPos1) + '_' + str(indexPiece1) + '_' + str(
                                indexPos2) + '_' + str(indexPos3)
                            newPuzzle = [puzzleID, board.fen(), newMoveSet, origLevel]
                            df = pd.concat(
                                [df, pd.DataFrame([newPuzzle], columns=['generatedID', 'FEN', 'MoveSet', 'Level'])])
                            print(newPuzzle)
                    else:
                        newMoveSet = " ".join(moveSet)
                        puzzleID = str(origId) + '_' + str(indexPos1) + '_' + str(indexPiece1) + '_' + str(indexPos2) + '_' + str(indexPos3)
                        newPuzzle = [puzzleID, board.fen(), newMoveSet, origLevel]
                        df = pd.concat(
                            [df, pd.DataFrame([newPuzzle], columns=['generatedID', 'FEN', 'MoveSet', 'Level'])])
                        print(newPuzzle)
            else:
                newMoveSet = " ".join(moveSet)
                puzzleID = str(origId) + '_' + str(indexPos1) + '_' + str(indexPiece1) + '_' + str(
                    indexPos2) + '_' + str(indexPos3)
                newPuzzle = [puzzleID, board.fen(), newMoveSet, origLevel]
                df = pd.concat(
                    [df, pd.DataFrame([newPuzzle], columns=['generatedID', 'FEN', 'MoveSet', 'Level'])])
                print(newPuzzle)
    return df

def generate(puzzleOrig):
    if 'mateIn2' in puzzleOrig[7].split():
        return generateMateIn2(puzzleOrig)
    elif 'mateIn3' in puzzleOrig[7].split():
        return generateMateIn3(puzzleOrig)


def main():
    index = input("Enter puzzle Id:\t")
    puzzle_manager = PuzzleManager.Puzzle(index)
    puzzle = puzzle_manager.parse()
    df_generated = generate(puzzle)
    print(df_generated)
    # df_generated.to_csv('Generated', mode='a')


if __name__ == "__main__":
    main()