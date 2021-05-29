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


class PowTestCase(unittest.TestCase):
    def test_numbers(self):
        self.assertEqual(9, builtin_impls.my_pow(3, 2))

    def test_negative(self):
        self.assertEqual(None, builtin_impls.my_pow(3, -2))

    def test_zero(self):
        self.assertEqual(1, builtin_impls.my_pow(3, 0))

    def test_one(self):
        self.assertEqual(3, builtin_impls.my_pow(3, 1))

    def test_big_value(self):
        self.assertEqual(3 ** 4, builtin_impls.my_pow(3, 4))


class AnyTestCase(unittest.TestCase):
    def test_any_true(self):
        self.assertEqual(True, builtin_impls.my_any([False, True, False]))

    def test_any_false(self):
        self.assertEqual(False, builtin_impls.my_any([False, False]))

    def test_empty(self):
        self.assertEqual(False, builtin_impls.my_any([]))


class AllTestCase(unittest.TestCase):
    def test_all_true(self):
        self.assertEqual(True, builtin_impls.my_all([True, True, True]))

    def test_all_false(self):
        self.assertEqual(False, builtin_impls.my_all([True, False, False]))

    def test_empty(self):
        self.assertEqual(True, builtin_impls.my_all([]))


class ReversedTestCase(unittest.TestCase):
    def test_list(self):
        self.assertEqual([2, 3, 7], builtin_impls.my_reversed([7, 3, 2]))


class RangeTestCase(unittest.TestCase):
    def test_list(self):
        self.assertEqual([1, 2], builtin_impls.my_range(1, 3, 1))

    def test_end_less_than_start(self):
        self.assertEqual([1], builtin_impls.my_range(1, 0, -1))

    def test_end_equal_to_start(self):
        self.assertEqual(None, builtin_impls.my_range(1, 1, 1))


if __name__ == "__main__":
    unittest.main()
