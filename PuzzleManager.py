import pandas as pd


class Puzzle:
    df_mateIn2 = pd.read_csv('mateIn2WithLevel.csv')

    def __init__(self, puzzle_id):
        self.id = puzzle_id

    def parse(self):
        try:
            return self.df_mateIn2.loc[self.df_mateIn2['PuzzleId'] == self.id].to_numpy().tolist()[0]
        except KeyError:
            return f'Элемент с ID {id} не найден.'