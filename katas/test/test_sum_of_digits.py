import unittest
from katas.sum_of_digits import sum_of_digits

class TestSumOfDigits(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(sum_of_digits("abc123"), 6)

    def test_with_text_and_digits(self):
        self.assertEqual(sum_of_digits("5 cats and 2 dogs"), 7)

    def test_no_digits(self):
        self.assertEqual(sum_of_digits("No digits here!"), 0)

    def test_with_negative_signs(self):
        # Just ignores the '-' signs if you're not parsing negatives
        self.assertEqual(sum_of_digits("abc-1-2-3"), 6)

if __name__ == '__main__':
    unittest.main()
