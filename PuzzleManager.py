import numpy as np
import pandas as pd


class Puzzle:
    df_mateIn2 = pd.read_csv('mateIn2WithLevel.csv')

    def __init__(self, n):
        self.n = n

    def parse(self):
        puzzle = self.df_mateIn2[self.df_mateIn2['Level'] == self.n].sample(n=1).to_numpy().tolist()[0]
        puzzle = [puzzle[0], puzzle[1], puzzle[2], puzzle[10]]
        return puzzle
