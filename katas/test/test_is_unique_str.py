import unittest
from katas.is_unique_str import is_unique


class TestIsUnique(unittest.TestCase):
    def test_is_unique_with_duplicates(self):
        self.assertFalse(is_unique("Hello"))  # 'l' is repeated

    def test_is_unique_all_unique(self):
        self.assertTrue(is_unique("World"))   # all letters are unique
        self.assertTrue(is_unique("Python"))
        self.assertTrue(is_unique("Unique"))  # 'u' appears twice but different case not handled

    def test_empty_string(self):
        self.assertTrue(is_unique(""))  # Empty string should return True

    def test_single_character(self):
        self.assertTrue(is_unique("A"))  # Only one character, should return True

    def test_numbers_and_symbols(self):
        self.assertTrue(is_unique("123!@#"))
        self.assertFalse(is_unique("1123"))  # '1' is repeated

    def test_case_sensitive(self):
        self.assertTrue(is_unique("aA"))  # Case-sensitive: 'a' and 'A' are different
        self.assertFalse(is_unique("AaAa"))  # Repeated pattern

    def test_long_non_unique_string(self):
        self.assertFalse(is_unique("abcdefghijklmnopqrstuvwxyzAabcdefghijklmnopqrstuvwxyz"))

    def test_long_unique_string(self):
        self.assertTrue(is_unique("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"))

if __name__ == '__main__':
    unittest.main()
