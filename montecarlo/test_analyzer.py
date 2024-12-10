import unittest
import pandas as pd
from .game import Game, Die
from .analyzer import Analyzer

class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        # Create some Die objects for testing
        self.die1 = Die(6)
        self.die2 = Die(6)
        self.die3 = Die(6)

        # Create a Game object
        self.game = Game([self.die1, self.die2, self.die3])
        self.game.play(5)  # Roll the dice 5 times
        
        # Create an Analyzer object
        self.analyzer = Analyzer(self.game)

    def test_initialization_with_invalid_game(self):
        with self.assertRaises(ValueError):
            Analyzer("invalid input")  # Invalid input should raise ValueError

    def test_face_counts_per_roll(self):
        self.analyzer.results = pd.DataFrame({
            0: ['1', '2', '1', '3', '1'],
            1: ['1', '1', '2', '3', '1'],
            2: ['1', '1', '2', '3', '1'],
        })
        expected_counts = pd.DataFrame({'Roll Number': [0, 1, 2, 3, 4], '1': [3, 2, 3, 0, 3]})
        result_df = self.analyzer.face_counts_per_roll('1')
        pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_counts)

    def test_combo_count(self):
        self.analyzer.results = pd.DataFrame({
            0: ['1', '1', '2', '3', '3'],
            1: ['1', '1', '2', '3', '3'],
            2: ['1', '1', '2', '3', '3'],
        })
        expected_combos = pd.DataFrame({'Count': [3, 2]}, index=[('1', '1', '1'), ('2', '3', '3')])
        expected_combos.index.name = 'Combination'
        combo_df = self.analyzer.combo_count()
        pd.testing.assert_frame_equal(combo_df.sort_index(), expected_combos.sort_index())

    def test_permutation_count(self):
        self.analyzer.results = pd.DataFrame({
            0: ['1', '1', '2', '3', '3'],
            1: ['1', '1', '2', '3', '3'],
            2: ['1', '1', '2', '3', '3'],
        })
        expected_perms = {
            ('1', '1', '1'): 3,
            ('3', '3', '2'): 2,
            ('3', '2', '3'): 2,
            ('2', '3', '3'): 2,
            # Ensure all expected permutations are included
        }
        perm_df = self.analyzer.permutation_count()
        for perm, count in expected_perms.items():
            self.assertEqual(perm_df.loc[perm, 'Count'], count)

    def test_jackpot(self):
        self.analyzer.results = pd.DataFrame({
            0: [1, 1, 1, 1, 1],  # All the same, so this should count as a jackpot
            1: [1, 1, 1, 1, 1],
            2: [1, 1, 1, 1, 1],
        })
        self.assertEqual(self.analyzer.jackpot(), 5)  # All rolls are jackpots

if __name__ == '__main__':
    unittest.main()

