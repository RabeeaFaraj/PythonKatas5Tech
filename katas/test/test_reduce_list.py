import unittest
from katas.reduce_list import reduce_array

class TestReduceArray(unittest.TestCase):

    def test_reduce_array_basic(self):
        self.assertEqual(reduce_array([10, 15, 7, 20, 25]), [10, 5, -8, 13, 5])

    def test_reduce_array_single_element(self):
        self.assertEqual(reduce_array([42]), [42])

    def test_reduce_array_two_elements(self):
        self.assertEqual(reduce_array([5, 8]), [5, 3])

    def test_reduce_array_negative_numbers(self):
        self.assertEqual(reduce_array([-3, -1, -4]), [-3, 2, -3])

    def test_reduce_array_zeros(self):
        self.assertEqual(reduce_array([0, 0, 0]), [0, 0, 0])

if __name__ == '__main__':
    unittest.main()
