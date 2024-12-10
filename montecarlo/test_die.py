import unittest
import numpy as np
import pandas as pd
from .die import Die

class TestDie(unittest.TestCase):
    def setUp(self):
        self.faces = np.array([1, 2, 3, 4, 5, 6])
        self.die = Die(self.faces)

    def test_initialization(self):
        with self.assertRaises(TypeError):
            Die([1, 2, 3])  # List instead of NumPy array
        with self.assertRaises(ValueError):
            Die(np.array([1, 2, 2]))  # Duplicate faces
        self.assertIsInstance(self.die, Die)

    def test_change_weight(self):
        self.die.change_weight(1, 10)
        self.assertEqual(self.die.show_state().loc[1, 'Weight'], 10)
        with self.assertRaises(IndexError):
            self.die.change_weight(7, 10)  # Invalid face
        with self.assertRaises(TypeError):
            self.die.change_weight(1, "invalid")  # Non-numeric weight

    def test_roll(self):
        outcomes = self.die.roll(10)
        self.assertEqual(len(outcomes), 10)
        with self.assertRaises(ValueError):
            self.die.roll(0)  # Invalid roll count

    def test_show_state(self):
        state = self.die.show_state()
        self.assertIsInstance(state, pd.DataFrame)
        self.assertFalse(state is self.die.show_state())  # Ensure it's a copy

if __name__ == '__main__':
    unittest.main()

