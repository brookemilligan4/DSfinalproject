import unittest
import numpy as np
import pandas as pd

class testAnalyzer(unittest.TestCase):
    def setUp(self):
        # Common setup for tests in testAnalyzer
        self.test_faces = np.array([1, 2, 3, 4, 5, 6])
    
    def test_analyzer_initialization(self):
        # Test analyzer initialization
        dice = [Die(self.test_faces), Die(self.test_faces)]
        game = Game(dice)
        game.play(10)
        analyzer = Analyzer(game)
        self.assertTrue(isinstance(analyzer, Analyzer))
    
    def test_analyzer_jackpot(self):
        # Test jackpot method
        dice = [Die(np.array([1])), Die(np.array([1]))]
        game = Game(dice)
        game.play(10)
        analyzer = Analyzer(game)
        self.assertEqual(analyzer.jackpot(), 10)
    
    def test_analyzer_face_counts(self):
        # Test face counts per roll
        dice = [Die(self.test_faces), Die(self.test_faces)]
        game = Game(dice)
        game.play(10)
        analyzer = Analyzer(game)
        face_counts = analyzer.face_counts_per_roll()
        self.assertEqual(face_counts.shape[0], 10)
    
    def test_analyzer_combo(self):
        # Test combination counting
        dice = [Die(self.test_faces), Die(self.test_faces)]
        game = Game(dice)
        game.play(10)
        analyzer = Analyzer(game)
        combos = analyzer.combo()
        self.assertTrue(isinstance(combos, pd.DataFrame))
    
    def test_analyzer_permutation(self):
        # Test permutation counting
        dice = [Die(self.test_faces), Die(self.test_faces)]
        game = Game(dice)
        game.play(10)
        analyzer = Analyzer(game)
        perms = analyzer.permutation()
        self.assertTrue(isinstance(perms, pd.DataFrame))
def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(testAnalyzer)
    runner = unittest.TextTestRunner()
    runner.run(suite)

run_tests()

