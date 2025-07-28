import unittest
from katas.longest_common_prefix import longest_common_prefix


class TestLongestCommonPrefix(unittest.TestCase):

    def test_common_prefix_exists(self):
        self.assertEqual(longest_common_prefix(["flower", "flow", "flight"]), "fl")

    def test_no_common_prefix(self):
        self.assertEqual(longest_common_prefix(["dog", "racecar", "car"]), "")

    def test_full_word_common_prefix(self):
        self.assertEqual(longest_common_prefix(["apple", "apple", "apple"]), "apple")

    def test_partial_common_prefix(self):
        self.assertEqual(longest_common_prefix(["apple", "apricot", "ape"]), "ap")

    def test_single_word(self):
        self.assertEqual(longest_common_prefix(["banana"]), "banana")

    def test_empty_list(self):
        self.assertEqual(longest_common_prefix([]), "")

    def test_one_empty_string(self):
        self.assertEqual(longest_common_prefix(["", "b", "bc"]), "")

    def test_all_empty_strings(self):
        self.assertEqual(longest_common_prefix(["", "", ""]), "")

    def test_common_prefix_long_words(self):
        self.assertEqual(longest_common_prefix(["interspecies", "interstellar", "interstate"]), "inters")

if __name__ == '__main__':
    unittest.main()
