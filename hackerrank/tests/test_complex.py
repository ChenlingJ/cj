import textwrap
import unittest

from hackerrank.complex import solve


class ComplexTestCase(unittest.TestCase):
    def test_sample(self):
        x = (2, 1)
        y = (5, 6)

        expected = textwrap.dedent(
            """
            7.00+7.00i
            -3.00-5.00i
            4.00+17.00i
            0.26-0.11i
            2.24+0.00i
            7.81+0.00i
            """
        ).strip()

        actual = solve(x, y)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
