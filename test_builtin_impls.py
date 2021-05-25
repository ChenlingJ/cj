import unittest

import builtin_impls


class MaxTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(None, builtin_impls.my_max([]))

    def test_empty_range(self):
        self.assertEqual(None, builtin_impls.my_max(range(0)))

    def test_empty_iter(self):
        self.assertEqual(None, builtin_impls.my_max(iter([])))

    def test_range(self):
        self.assertEqual(6, builtin_impls.my_max(range(7)))

    def test_all_negative(self):
        self.assertEqual(-3, builtin_impls.my_max([-4, -3, -51, -30]))

    def test_mixed_numbers(self):
        self.assertEqual(42, builtin_impls.my_max((4, -1, 42, -100, -3, 23)))


if __name__ == "__main__":
    unittest.main()
