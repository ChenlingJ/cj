import unittest

from hackerrank.interviewprep.warmup import repeated_string
from hackerrank.interviewprep.tests import patch_io


class MyTestCase(unittest.TestCase):
    def test_something(self):
        output_lines = patch_io(
            repeated_string,
            """
            aaaaaaaa
            151
            """,
        )

        repeated_string.main()

        expected_output = "151"
        actual_output = "\n".join(output_lines)

        self.assertEqual(expected_output, actual_output)

    def test_way_too_long(self):
        output_lines = patch_io(
            repeated_string,
            """
            a
            100000000000
            """,
        )

        repeated_string.main()

        expected_output = "100000000000"
        actual_output = "\n".join(output_lines)

        self.assertEqual(expected_output, actual_output)


if __name__ == "__main__":
    unittest.main()
