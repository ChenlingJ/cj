import textwrap
import unittest

from hackerrank.alphabet_rangoli import rangoli


class TestAlphabetRangoli(unittest.TestCase):
    def test_size3(self):
        actual = rangoli(3)
        expected = textwrap.dedent("""\
            ----c----
            --c-b-c--
            c-b-a-b-c
            --c-b-c--
            ----c----
            """.rstrip())

        self.assertEqual(actual, expected)

    def test_size5(self):
        actual = rangoli(5)
        expected = textwrap.dedent("""\
            --------e--------
            ------e-d-e------
            ----e-d-c-d-e----
            --e-d-c-b-c-d-e--
            e-d-c-b-a-b-c-d-e
            --e-d-c-b-c-d-e--
            ----e-d-c-d-e----
            ------e-d-e------
            --------e--------
            """.rstrip())

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
