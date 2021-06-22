from random import shuffle

import unittest

from algorithms.sorting.common import is_sorted


class BogoSortTest(unittest.TestCase):
    def test_empty(self):
        self.do_test([])

    def test_shuffled_3(self):
        items = list(range(3))
        shuffle(items)
        self.do_test(items)

    def test_shuffled_4(self):
        items = list(range(4))
        shuffle(items)
        self.do_test(items)

    def test_shuffled_5(self):
        items = list(range(5))
        shuffle(items)
        self.do_test(items)

    def test_shuffled_6(self):
        items = list(range(6))
        shuffle(items)
        self.do_test(items)

    def test_shuffled_7(self):
        items = list(range(7))
        shuffle(items)
        self.do_test(items)

    def test_shuffled_8(self):
        items = list(range(8))
        shuffle(items)
        self.do_test(items)

    def test_shuffled_9(self):
        items = list(range(9))
        shuffle(items)
        self.do_test(items)

    def test_shuffled_10(self):
        items = list(range(10))
        shuffle(items)
        self.do_test(items)

    def do_test(self, items: list[int]):
        expected = list(sorted(items))
        bogo_sort(items)
        self.assertListEqual(expected, items)


def bogo_sort(items: list[int]):
    """
    Sort a list. This algorithm is a joke, and is inefficient on purpose.
    Worst case: O(infinity)
    """
    # def is_sorted():
    #     for i in range(len(items) - 1):
    #         if items[i] > items[i + 1]:
    #             return False
    #     return True

    while not is_sorted(items):
        shuffle(items)


if __name__ == "__main__":
    unittest.main()
