import textwrap
import unittest

from hackerrank import alphabet_rangoli


class _TestBase(unittest.TestCase):
    def __init__(self, fn, *args, **kwargs):
        super(_TestBase, self).__init__(*args, *kwargs)
        self.rangoli_fn = fn

    def test_size1(self):
        actual = self.rangoli_fn(1)
        expected = "a"

        self.assertEqual(actual, expected)

    def test_size2(self):
        actual = self.rangoli_fn(2)
        expected = textwrap.dedent(
            """
            --b--
            b-a-b
            --b--
            """
        ).strip()

        self.assertEqual(actual, expected)

    def test_size3(self):
        actual = self.rangoli_fn(3)
        expected = textwrap.dedent(
            """
            ----c----
            --c-b-c--
            c-b-a-b-c
            --c-b-c--
            ----c----
            """
        ).strip()

        self.assertEqual(actual, expected)

    def test_size5(self):
        actual = self.rangoli_fn(5)
        expected = textwrap.dedent(
            """
            --------e--------
            ------e-d-e------
            ----e-d-c-d-e----
            --e-d-c-b-c-d-e--
            e-d-c-b-a-b-c-d-e
            --e-d-c-b-c-d-e--
            ----e-d-c-d-e----
            ------e-d-e------
            --------e--------
            """
        ).strip()

        self.assertEqual(actual, expected)

    def test_size10(self):
        actual = self.rangoli_fn(10)
        expected = textwrap.dedent(
            """
            ------------------j------------------
            ----------------j-i-j----------------
            --------------j-i-h-i-j--------------
            ------------j-i-h-g-h-i-j------------
            ----------j-i-h-g-f-g-h-i-j----------
            --------j-i-h-g-f-e-f-g-h-i-j--------
            ------j-i-h-g-f-e-d-e-f-g-h-i-j------
            ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
            --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
            j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
            --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
            ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
            ------j-i-h-g-f-e-d-e-f-g-h-i-j------
            --------j-i-h-g-f-e-f-g-h-i-j--------
            ----------j-i-h-g-f-g-h-i-j----------
            ------------j-i-h-g-h-i-j------------
            --------------j-i-h-i-j--------------
            ----------------j-i-j----------------
            ------------------j------------------
            """
        ).strip()

        self.assertEqual(actual, expected)


class TestAlphabetRangoli(_TestBase):
    def __init__(self, *args, **kwargs):
        super(TestAlphabetRangoli, self).__init__(
            alphabet_rangoli.rangoli, *args, **kwargs
        )


class TestAlphabetRangoli2(_TestBase):
    def __init__(self, *args, **kwargs):
        super(TestAlphabetRangoli2, self).__init__(
            alphabet_rangoli.rangoli2, *args, **kwargs
        )


if __name__ == "__main__":
    unittest.main()
