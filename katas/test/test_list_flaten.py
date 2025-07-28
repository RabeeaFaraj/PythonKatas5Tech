import unittest
from katas.list_flatten import flatten_list


class TestFlattenList(unittest.TestCase):

    def test_flatten_basic(self):
        nested = [1, [2, 3], [4, [5, 6]], 7]
        expected = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(flatten_list(nested), expected)

    def test_flatten_single_level(self):
        nested = [1, 2, 3]
        expected = [1, 2, 3]
        self.assertEqual(flatten_list(nested), expected)

    def test_flatten_deep_nesting(self):
        nested = [[[[1]], 2], [[3, [4]]]]
        expected = [1, 2, 3, 4]
        self.assertEqual(flatten_list(nested), expected)

    def test_flatten_empty_list(self):
        nested = []
        expected = []
        self.assertEqual(flatten_list(nested), expected)

    def test_flatten_nested_empty_lists(self):
        nested = [[], [[]], [[[]]], 1]
        expected = [1]
        self.assertEqual(flatten_list(nested), expected)

    def test_flatten_only_empty_lists(self):
        nested = [[], [[]], [[[]]]]
        expected = []
        self.assertEqual(flatten_list(nested), expected)


if __name__ == '__main__':
    unittest.main()
