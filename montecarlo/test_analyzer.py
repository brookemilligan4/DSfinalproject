import unittest
import pandas as pd
from game import Game, Die
from analyzer import Analyzer

class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        # Create some Die objects for testing
        self.die1 = Die(3)  # Assuming Die takes number of faces as an argument
        self.die2 = Die(3)
        self.die3 = Die(3)

        # Create a Game object
        self.game = Game([self.die1, self.die2, self.die3])
        self.game.play(5)  # Roll the dice 5 times
        
        # Create an Analyzer object
        self.analyzer = Analyzer(self.game)

    def test_initialization_with_invalid_game(self):
        with self.assertRaises(ValueError):
            Analyzer("invalid input")  # Invalid input should raise ValueError

    def test_jackpot(self):
        # Manually set results to test jackpot counts
        self.analyzer.results = pd.DataFrame({
            0: [1, 1, 1, 3, 3],
            1: [1, 1, 1, 3, 3],
            2: [1, 1, 1, 3, 3],
        })
        self.assertEqual(self.analyzer.jackpot(), 3)  # Three rolls are jackpots

    def test_face_counts_per_roll(self):
        # Manually set results to test face counts
        self.analyzer.results = pd.DataFrame({
            0: ['1', '1', '1', '3', '1'],
            1: ['1', '1', '2', '3', '1'],
            2: ['1', '2', '1', '3', '1'],
        })
        result_df = self.analyzer.face_counts_per_roll('1')
        expected_counts = pd.DataFrame({'Roll Number': [0, 1, 2, 3, 4], '1': [3, 2, 3, 0, 3]})
        pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_counts)

    def test_face_counts_per_roll_invalid_face(self):
        with self.assertRaises(ValueError):
            self.analyzer.face_counts_per_roll('7')  # Invalid face should raise ValueError

    def test_combo_count(self):
        # Manually set results to test combo counts
        self.analyzer.results = pd.DataFrame({
            0: ['1', '1', '2', '3', '3'],
            1: ['1', '1', '2', '3', '3'],
            2: ['1', '1', '2', '3', '3'],
        })
        combo_df = self.analyzer.combo_count()
        expected_df = pd.DataFrame({
            'Combination': [('1', '1', '1'), ('2', '2', '2'), ('3', '3', '3')],
            'Count': [3, 0, 2]
        }).set_index('Combination')
        pd.testing.assert_series_equal(combo_df['Count'], expected_df['Count'])

    def test_permutation_count(self):
        # Manually set results to test permutation counts
        self.analyzer.results = pd.DataFrame({
            0: ['1', '2', '1'],
            1: ['1', '1', '2'],
            2: ['2', '2', '1'],
        })
        perm_df = self.analyzer.permutation_count()
        self.assertIn(('1', '1', '1'), perm_df.index)  # Check if permutations include ('1', '1', '1')
        self.assertIn(('2', '2', '2'), perm_df.index)  # Check if permutations include ('2', '2', '2')

if __name__ == '__main__':
    unittest.main()

