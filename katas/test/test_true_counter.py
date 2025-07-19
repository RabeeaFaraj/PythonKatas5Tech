import unittest
from katas.true_counter import count_true_values

class TestTrueCounter(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(count_true_values([True, False, True, True, False]), 3)

    def test_empty_array(self):
        self.assertEqual(count_true_values([]), 0)

if __name__ == '__main__':
    unittest.main()
