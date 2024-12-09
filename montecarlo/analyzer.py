import pandas as pd
from collections import Counter
from itertools import permutations
from game import Game

class Analyzer:
    def __init__(self, game):
        if not isinstance(game, Game):
            raise ValueError("Input must be a Game object.")
        
        self.game = game
        self.results = self.game.show_results()
        self.results = self.results.astype(str)

    def jackpot(self):
        jackpot_count = 0
        for roll in self.results.itertuples(index=False):
            if len(set(roll)) == 1:
                jackpot_count += 1
        return jackpot_count

    def face_counts_per_roll(self, face):
        if face not in self.results.values:
            raise ValueError(f"Face '{face}' is not a valid face.")

        counts = self.results.apply(lambda x: (x == face).sum(), axis=1)
        return pd.DataFrame({'Roll Number': self.results.index, face: counts})

    def combo_count(self):
        combos = []
        for roll in self.results.itertuples(index=False):
            combos.append(tuple(sorted(roll)))

        combo_counts = Counter(combos)
        combo_df = pd.Series(combo_counts).reset_index(name='Count')
        combo_df.rename(columns={'index': 'Combination'}, inplace=True)
        combo_df.index.names = ['Combination']
        return combo_df

    def permutation_count(self):
        perms = []
        for roll in self.results.itertuples(index=False):
            perms.extend(permutations(roll))

        perm_counts = Counter(perms)
        perm_df = pd.DataFrame.from_dict(perm_counts, orient='index', columns=['Count'])
        perm_df.index.names = ['Permutation']
        return perm_df

