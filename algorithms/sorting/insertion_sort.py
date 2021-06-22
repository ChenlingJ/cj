import unittest
from random import shuffle


class InsertionSortTest(unittest.TestCase):
    def test_empty(self):
        self.do_test([])

    def test_ordered(self):
        self.do_test(list(range(10)))

    def test_shuffled_10(self):
        items = list(range(10))
        shuffle(items)
        self.do_test(items)

    def test_shuffled_100(self):
        items = list(range(100))
        shuffle(items)
        self.do_test(items)

    def test_shuffled_1000(self):
        items = list(range(1000))
        shuffle(items)
        self.do_test(items)

    def test_shuffled_2000(self):
        items = list(range(2000))
        shuffle(items)
        self.do_test(items)
    #
    # def test_shuffled_4k(self):
    #     items = list(range(4000))
    #     shuffle(items)
    #     self.do_test(items)

    def test_shuffled_10k(self):
        items = list(range(10_000))
        shuffle(items)
        self.do_test(items)

    # def test_shuffled_20k(self):
    #     items = list(range(20_000))
    #     shuffle(items)
    #     self.do_test(items)
    #
    # def test_shuffled_40k(self):
    #     items = list(range(40_000))
    #     shuffle(items)
    #     self.do_test(items)
    #
    # def test_ordered_4000(self):
    #     items = list(range(4000))
    #     self.do_test(items)
    #
    # def test_reversed_4000(self):
    #     items = list(reversed(range(4000)))
    #     self.do_test(items)

    def do_test(self, items: list[int]):
        expected = list(sorted(items))
        items = insertion_sort(items)
        self.assertListEqual(expected, items)


def insertion_sort(items: list[int]) -> list[int]:
    result = []
    for item in items:
        # i = 0
        # while i < len(result) and item > result[i]:
        #     i += 1
        # result.insert(i, item)

        # for i in range(len(result) + 1):
        #     if i == len(result) or result[i] > item:
        #         result.insert(i, item)
        #         break

        for i in range(len(result)):
            if result[i] > item:
                result.insert(i, item)
                break
        else:
            # If a `break` statement is never encountered, this `else` clause runs.
            result.append(item)

    return result

"""
item=2, result=[]
    i=0. i == len(result). insert at 0.
item=5, result=[2]
    i=0. i != len(result). result[i] <= item. next.
    i=1. i == len(result). insert at 1.
"""


"""
items=2 5 1 3 9 6 8 7 4
item=2 result=[], i=0
    i=0, no run
item=5 result[2]
    i=0, items[i]=2, 2 < 5
    i=1, no run
item=1 result=[2, 5], i=0. after insert, result=[1, 2, 5]
    i=0, items[i]=2, 1 < 2, no run
item=3 result=[1, 2, 5], i=2. after insert, result=[1, 2, 3, 5]
    i=0 items[i]=1, 3 > 1
    i=1 items[i]=2, 3 > 2
    i=2 items[i]=5, 3 < 5, no run
"""

#
# """
# 2 5 (1) 9 3 6 8 7 4
# 1 2 5 9 (3) 6 8 7 4
# 1 2 3 5 9 (6) 8 7 4
# """


if __name__ == "__main__":
    unittest.main()
