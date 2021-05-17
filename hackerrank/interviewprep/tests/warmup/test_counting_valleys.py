import unittest
from textwrap import dedent

from hackerrank.interviewprep.warmup import counting_valleys
from hackerrank.interviewprep.tests import patch_io


class MyTestCase(unittest.TestCase):
    def test_sample_input(self):
        output_lines = patch_io(
            counting_valleys,
            """
            8
            UDDDUDUU
            """,
        )

        counting_valleys.main()

        expected_output = "1"
        actual_output = "\n".join(output_lines)

        self.assertEqual(expected_output, actual_output)

    def test_custom_input(self):
        output_lines = patch_io(
            counting_valleys,
            """
            8
            DUDUDUDUDUUDUDUDUDUDDUDUDUDUDUUDUDUDUDUD
            """,
        )

        counting_valleys.main()

        expected_output = "10"
        actual_output = "\n".join(output_lines)

        self.assertEqual(expected_output, actual_output)


if __name__ == "__main__":
    unittest.main()
