import textwrap
import unittest

from hackerrank import alphabet_rangoli


class _TestBase(unittest.TestCase):
    def __init__(self, fn, *args, **kwargs):
        super(_TestBase, self).__init__(*args, *kwargs)
        self.rangoli_fn = fn

    def test_size3(self):
        actual = self.rangoli_fn.__call__(3)
        expected = textwrap.dedent("""\
            ----c----
            --c-b-c--
            c-b-a-b-c
            --c-b-c--
            ----c----
            """.rstrip())

        self.assertEqual(actual, expected)

    def test_size5(self):
        actual = self.rangoli_fn.__call__(5)
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


class TestAlphabetRangoli(_TestBase):
    def __init__(self, *args, **kwargs):
        super(TestAlphabetRangoli, self).__init__(alphabet_rangoli.rangoli, *args, **kwargs)


class TestAlphabetRangoli2(_TestBase):
    def __init__(self, *args, **kwargs):
        super(TestAlphabetRangoli2, self).__init__(alphabet_rangoli.rangoli2, *args, **kwargs)


if __name__ == '__main__':
    unittest.main()
