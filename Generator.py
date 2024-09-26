import random as rd

import chess
import pandas as pd

import Utils
import PuzzleManager


def generate(puzzleOrig):
    df = pd.DataFrame(columns=['PuzzleId', 'FEN', 'Moves', 'Level'])

    origId = puzzleOrig[0]
    origFen = puzzleOrig[1]
    origMoveSet = puzzleOrig[2].split()
    origLevel = puzzleOrig[3]
    origBoard = chess.Board(origFen)
    indexPos1 = 0
    indexPiece1 = 0
    indexPos2 = 0

    # генерация первого хода игрока
    board = origBoard.copy()
    humanPoses1 = Utils.getMovesToTarget(board, origMoveSet[1][0:2], origMoveSet[1][2:4])
    if origMoveSet[0][2:4] in humanPoses1:
        humanPoses1.remove(origMoveSet[0][2:4])
    for humanPose in humanPoses1[:]:
        moveSet = list(origMoveSet)
        piece = board.remove_piece_at(chess.parse_square(moveSet[1][0:2]))
        board.set_piece_at(humanPose, piece)
        if not board.is_legal(chess.Move.from_uci(moveSet[0])) or board.is_variant_end() or board.gives_check(chess.Move.from_uci(moveSet[0])):
            humanPoses1.remove(humanPose)
            continue
    for humanPose1 in humanPoses1:
        indexPos1 += 1
        moveSet = list(origMoveSet)
        moveSet[1] = chess.square_name(humanPose1) + moveSet[1][2:4]
        board = origBoard.copy()
        piece = board.remove_piece_at(chess.parse_square(moveSet[1][0:2]))
        board.set_piece_at(humanPose1, piece)
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
            board.set_piece_at(humanPose1, humanPiece)

        # генерация второго хода игрока
        if origMoveSet[1][2:4] != origMoveSet[3][0:2]:
            humanPoses2 = Utils.getMovesToTarget(board, moveSet[3][0:2], moveSet[3][2:4])
            if moveSet[0][2:4] in humanPoses2:
                humanPoses2.remove(moveSet[0][2:4])
            if moveSet[1][2:4] in humanPoses2:
                humanPoses2.remove(moveSet[1][2:4])
            if moveSet[2][2:4] in humanPoses2:
                humanPoses2.remove(moveSet[2][2:4])
            for humanPose2 in humanPoses2[:]:
                board2 = board.copy()
                piece = board2.remove_piece_at(chess.parse_square(moveSet[3][0:2]))
                board2.set_piece_at(humanPose2, piece)
                if board2.is_variant_end():
                    humanPoses2.remove(humanPose2)
                    continue
                board2.push(chess.Move.from_uci(moveSet[0]))
                if board2.is_variant_end():
                    humanPoses2.remove(humanPose2)
                    continue
                board2.push(chess.Move.from_uci(moveSet[1]))
                if board2.is_variant_end():
                    humanPoses2.remove(humanPose2)
                    continue
                if board2.is_check():
                    humanPoses2.remove(humanPose2)
                    continue
                board2.push(chess.Move.from_uci(moveSet[2]))
                if board2.is_variant_end():
                    humanPoses2.remove(humanPose2)
                    continue
                if board2.is_check():
                    humanPoses2.remove(humanPose2)
                    continue
            for humanPose2 in humanPoses2:
                indexPos2 += 1
                moveSet[3][0:2] = chess.square_name(humanPose2)
                piece = board.remove_piece_at(chess.parse_square(moveSet[3][0:2]))
                board.set_piece_at(humanPose2, piece)

        newMoveSet = " ".join(moveSet)
        puzzleID = str(origId) + '_' + str(indexPos1) + '_' + str(indexPiece1) + '_' + str(indexPos2)
        newPuzzle = [puzzleID, board.fen(), newMoveSet, origLevel]
        df = pd.concat([df, pd.DataFrame([newPuzzle])], ignore_index=True)
        print(newPuzzle)
    return df


def main():
    df_MateIn2_Generated = pd.DataFrame(columns=['PuzzleId', 'FEN', 'Moves', 'Level'])
    # df_MateIn2_Generated = pd.read_csv('mateIn2Generated')
    for i in range(1):
        puzzle_manager = PuzzleManager.Puzzle(4)
        puzzle = puzzle_manager.parse()
        df_MateIn2_Generated = pd.concat([df_MateIn2_Generated, generate(puzzle)], ignore_index=True)
    df_MateIn2_Generated.to_csv('mateIn2Generated')


if __name__ == "__main__":
    main()