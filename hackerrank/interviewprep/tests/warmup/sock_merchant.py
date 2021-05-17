import unittest
from textwrap import dedent

from hackerrank.interviewprep.warmup import sock_merchant
from hackerrank.interviewprep.tests import patch_io


class MyTestCase(unittest.TestCase):
    def test_something(self):
        output_lines = patch_io(
            sock_merchant,
            """
            9
            10 20 20 10 10 30 50 10 20
            """,
        )

        sock_merchant.main()

        expected_output = "3"
        actual_output = "\n".join(output_lines)

        self.assertEqual(expected_output, actual_output)


if __name__ == "__main__":
    unittest.main()
