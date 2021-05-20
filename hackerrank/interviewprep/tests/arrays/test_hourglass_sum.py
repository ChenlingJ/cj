import unittest

from hackerrank.interviewprep.arrays import hourglass_sum
from hackerrank.interviewprep.tests import patch_io


class MyTestCase(unittest.TestCase):
    def test_sample_0(self):
        output_lines = patch_io(
            hourglass_sum,
            """
            1 1 1 0 0 0
            0 1 0 0 0 0
            1 1 1 0 0 0
            0 0 2 4 4 0
            0 0 0 2 0 0
            0 0 1 2 4 0
            """,
        )

        hourglass_sum.main()

        expected_output = "19"
        actual_output = "\n".join(output_lines)

        self.assertEqual(expected_output, actual_output)

    def test_sample_1(self):
        output_lines = patch_io(
            hourglass_sum,
            """
            -9 -9 -9  1 1 1 
             0 -9  0  4 3 2
            -9 -9 -9  1 2 3
             0  0  8  6 6 0
             0  0  0 -2 0 0
             0  0  1  2 4 0
            """,
        )

        hourglass_sum.main()

        expected_output = "28"
        actual_output = "\n".join(output_lines)

        self.assertEqual(expected_output, actual_output)


if __name__ == "__main__":
    unittest.main()
