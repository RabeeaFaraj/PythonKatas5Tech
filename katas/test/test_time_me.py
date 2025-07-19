import unittest
import time
from io import StringIO
import sys

from katas.time_me import measure_execution_time, sample_function, quick_function

class TestMeasureExecutionTime(unittest.TestCase):

    def test_sample_function_time(self):
        """Test that sample_function takes about 500 ms (±100 ms)."""
        duration = measure_execution_time(sample_function)
        self.assertTrue(400 <= duration <= 600,
                        f"Expected around 500ms, but got {duration:.2f}ms")

    def test_quick_function_time(self):
        """Test that quick_function takes less than 50 ms."""
        duration = measure_execution_time(quick_function)
        self.assertTrue(duration < 50,
                        f"Expected less than 50ms, but got {duration:.2f}ms")

    def test_quick_function_output(self):
        """Ensure quick_function prints the correct message."""
        captured_output = StringIO()
        sys.stdout = captured_output
        quick_function()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Quick task done!")

if __name__ == '__main__':
    unittest.main()
