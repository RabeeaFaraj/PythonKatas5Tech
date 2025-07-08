import unittest
from katas.is_unique_str import is_unique


class TestIsUnique(unittest.TestCase):
    def test_is_unique(self):
        self.assertEqual(is_unique(), True)
