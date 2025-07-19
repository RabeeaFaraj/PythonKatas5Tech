import unittest
from katas.list_diff import find_difference

class TestFindDifference(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(find_difference([10, 3, 5, 6, 20, -2]), 22)

    def test_all_same_numbers(self):
        self.assertEqual(find_difference([5, 5, 5, 5]), 0)

    def test_single_element(self):
        self.assertEqual(find_difference([42]), 0)

    def test_negative_numbers(self):
        self.assertEqual(find_difference([-10, -20, -30, -5]), 25)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            find_difference([])

if __name__ == '__main__':
    unittest.main()
