import unittest
import numpy as np
import pandas as pd
from your_module import Die, Game, Analyzer  # Replace 'your_module' with the actual module name

class TestDie(unittest.TestCase):

    def setUp(self):
        # Set up a valid die
        self.faces = np.array([1, 2, 3, 4, 5, 6])
        self.die = Die(self.faces)

    def test_initialization_valid(self):
        self.assertIsInstance(self.die._die_df, pd.DataFrame)
        self.assertEqual(len(self.die._die_df), len(self.faces))
        self.assertTrue(np.array_equal(self.die._die_df.index.values, self.faces))

    def test_initialization_invalid_faces_type(self):
        with self.assertRaises(TypeError):
            Die([1, 2, 3, 4, 5, 6])  # List instead of np.ndarray

    def test_initialization_invalid_faces_distinct(self):
        with self.assertRaises(ValueError):
            Die(np.array([1, 2, 2]))  # Non-distinct values

    def test_change_weight_valid(self):
        self.die.change_weight(1, 5)
        self.assertEqual(self.die._die_df.loc[1, 'Weight'], 5)

    def test_change_weight_invalid_face(self):
        with self.assertRaises(IndexError):
            self.die.change_weight(7, 5)  # Face not in the die

    def test_change_weight_invalid_weight(self):
        with self.assertRaises(TypeError):
            self.die.change_weight(1, "five")  # Invalid weight type

    def test_roll_valid(self):
        outcomes = self.die.roll(10)
        self.assertEqual(len(outcomes), 10)

    def test_roll_invalid_times(self):
        with self.assertRaises(ValueError):
            self.die.roll(0)  # Invalid number of rolls

    def test_show_state(self):
        state = self.die.show_state()
        self.assertIsInstance(state, pd.DataFrame)

class TestGame(unittest.TestCase):

    def setUp(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        self.die1 = Die(faces)
        self.die2 = Die(faces)
        self.game = Game([self.die1, self.die2])

    def test_initialization_valid(self):
        self.assertIsInstance(self.game.dice, list)
        self.assertEqual(len(self.game.dice), 2)

    def test_initialization_invalid(self):
        with self.assertRaises(TypeError):
            Game("not_a_list")  # Invalid input type

    def test_play_valid(self):
        self.game.play(5)
        self.assertIsInstance(self.game._last_play_results, pd.DataFrame)

    def test_play_invalid_rolls(self):
        with self.assertRaises(ValueError):
            self.game.play(0)  # Invalid number of rolls

    def test_show_results_no_play(self):
        with self.assertRaises(ValueError):
            self.game.show_results()  # No results available yet

    def test_get_results_wide(self):
        self.game.play(5)
        results = self.game.get_results(form='wide')
        self.assertIsInstance(results, pd.DataFrame)

    def test_get_results_narrow(self):
        self.game.play(5)
        results = self.game.get_results(form='narrow')
        self.assertIsInstance(results, pd.DataFrame)

    def test_get_results_invalid_form(self):
        with self.assertRaises(ValueError):
            self.game.get_results(form='invalid')  # Invalid form

class TestAnalyzer(unittest.TestCase):

    def setUp(self):
        faces = np.array([1, 2, 3, 4, 5, 6])
        die = Die(faces)
        game = Game([die])
        game.play(5)  # Play the game to generate results
        self.analyzer = Analyzer(game)

    def test_initialization_valid(self):
        self.assertIsInstance(self.analyzer.results, pd.DataFrame)

    def test_initialization_invalid(self):
        with self.assertRaises(ValueError):
            Analyzer("not_a_game")  # Invalid input type

    def test_jackpot(self):
        jackpot_count = self.analyzer.jackpot()
        self.assertIsInstance(jackpot_count, int)

    def test_face_counts_per_roll_valid(self):
        counts = self.analyzer.face_counts_per_roll(1)
        self.assertIsInstance(counts, pd.DataFrame)

    def test_face_counts_per_roll_invalid_face(self):
        with self.assertRaises(ValueError):
