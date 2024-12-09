import unittest
import pandas as pd
from game import Game, Die
from analyzer import Analyzer

class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        self.die1 = Die(3)
        self.die2 = Die(3)
        self.die3 = Die(3)
        self.game = Game([self.die1, self.die2, self.die3])
        self.game.play(5)
        self.analyzer = Analyzer(self.game)

    def test_initialization_with_invalid_game(self):
        with self.assertRaises(ValueError):
            Analyzer("invalid input")

    def test_jackpot(self):
        # Set results to have three jackpots
        self.analyzer.results = pd.DataFrame({
            0: ['1', '1', '1', '2', '2'],
            1: ['1', '1', '1', '2', '2'],
            2: ['1', '1', '1', '2', '2'],
        })
        self.assertEqual(self.analyzer.jackpot(), 3)

    def test_face_counts_per_roll(self):
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
            self.analyzer.face_counts_per_roll('7')

    def test_combo_count(self):
        self.analyzer.results = pd.DataFrame({
            0: ['1', '1', '2'],
            1: ['1', '1', '2'],
            2: ['1', '1', '2'],
        })
        combo_df = self.analyzer.combo
