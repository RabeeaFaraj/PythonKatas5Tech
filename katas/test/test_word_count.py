import unittest
from katas.word_count import count_words

class TestWordCount(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(count_words("This is a sample sentence for counting words."), 8)

    def test_empty_string(self):
        self.assertEqual(count_words(""), 0)

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(count_words("   Hello world   "), 2)

    def test_multiple_spaces_between_words(self):
        self.assertEqual(count_words("This   has  extra   spaces"), 4)

    def test_tabs_and_newlines(self):
        self.assertEqual(count_words("This\tis\na test"), 4)

    def test_punctuation_attached(self):
        self.assertEqual(count_words("Hello, world! This is a test."), 6)

if __name__ == '__main__':
    unittest.main()
