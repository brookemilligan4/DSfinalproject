import unittest
import pandas as pd
from .game import Game, Die 

class TestGame(unittest.TestCase):
    def setUp(self):
        # Create some Die objects for testing
        self.die1 = Die(6)  # Assuming Die takes number of faces as an argument
        self.die2 = Die(6)
        self.die3 = Die(6)
        self.game = Game([self.die1, self.die2])

    def test_initialization_with_invalid_dice(self):
        with self.assertRaises(ValueError):  # Change TypeError to ValueError
            Game("invalid input")
        with self.assertRaises(ValueError):
            Game([self.die1])  # Only one die should raise ValueError
        with self.assertRaises(ValueError):
            Game([self.die1, Die(8)])  # Different number of faces should raise ValueError

    def test_play_with_invalid_rolls(self):
        with self.assertRaises(ValueError):
            self.game.play(0)  # Rolls must be at least 1

    def test_play_and_show_results(self):
        self.game.play(5)  # Roll the dice 5 times
        results = self.game.show_results()
        self.assertEqual(len(results), 5)  # Check if there are 5 rolls
        self.assertEqual(results.shape[1], 2)  # Check if there are 2 dice

    def test_get_results_wide(self):
        self.game.play(3)
        wide_results = self.game.get_results('wide')
        self.assertTrue(isinstance(wide_results, pd.DataFrame))

    def test_get_results_narrow(self):
        self.game.play(3)
        narrow_results = self.game.get_results('narrow')
        self.assertTrue(isinstance(narrow_results, pd.DataFrame))
        self.assertEqual(narrow_results.shape[1], 2)  # Check if there are two columns: Die and Outcome

    def test_get_results_invalid_form(self):
        with self.assertRaises(ValueError):
            self.game.get_results('invalid_form')  # Invalid form should raise ValueError

if __name__ == '__main__':
    unittest.main()

