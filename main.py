import chess
from PuzzleManager import Puzzle

puzzle_manager = Puzzle(4)
puzzle = puzzle_manager.parse()
print(puzzle)
board = chess.Board(fen=puzzle[1])
print(board)

