import unittest
import numpy as np

class testDie(unittest.TestCase):
    def setUp(self):
        # Common setup for tests in testDie
        self.test_faces = np.array([1, 2, 3, 4, 5, 6])
        self.test_die = Die(self.test_faces)
    
    def test_die_initialization(self):
        # Test die initialization
        self.assertTrue(isinstance(self.test_die, Die))
        self.assertTrue(np.array_equal(self.test_die.show()['faces'], self.test_faces))
            
    def test_die_change_weight(self):
        # Test changing die weight
        self.test_die.change_weight(1, 2.0)
        weights = self.test_die.show()['weights']
        self.assertEqual(weights[1], 2.0)
    
    def test_die_invalid_weight(self):
        with self.assertRaises(TypeError):
            self.test_die.change_weight(1, "not_a_number")

    def test_die_roll(self):
        # Test die rolling
        rolls = self.test_die.roll(10)
        self.assertEqual(len(rolls), 10)
        self.assertTrue(all(roll in self.test_faces for roll in rolls))

def run_tests():
    suite = unittest.TestLoader().loadTestsFromTestCase(testDie)
    runner = unittest.TextTestRunner()
    runner.run(suite)

run_tests()
