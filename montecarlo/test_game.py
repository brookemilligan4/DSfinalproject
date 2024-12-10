import unittest
import numpy as np
import pandas as pd

class testGame(unittest.TestCase):
    def setUp(self):
        # Common setup for tests in testGame
        self.test_faces = np.array([1, 2, 3, 4, 5, 6])
    
    def test_game_initialization(self):
        # Test game initialization
        dice = [Die(self.test_faces), Die(self.test_faces)]
        game = Game(dice)
        self.assertTrue(isinstance(game, Game))
    
    def test_game_play(self):
        # Test game play
        dice = [Die(self.test_faces), Die(self.test_faces)]
        game = Game(dice)
        game.play(5)
        results = game.show()
        self.assertEqual(results.shape, (5, 2))

    def test_game_no_dice(self):
        with self.assertRaises(ValueError):
            Game([])
    
    def test_game_show_narrow(self):
        # Test game show in narrow format
        dice = [Die(self.test_faces), Die(self.test_faces)]
        game = Game(dice)
        game.play(5)
        narrow_results = game.show('narrow')
        self.assertTrue(isinstance(narrow_results.index, pd.MultiIndex))

    def test_game_invalid_show_format(self):
        dice = [Die(self.test_faces), Die(self.test_faces)]
        game = Game(dice)
        game.play(5)
        with self.assertRaises(ValueError):
            game.show("invalid_format")

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(testGame)
    runner = unittest.TextTestRunner()
    runner.run(suite)

run_tests()
