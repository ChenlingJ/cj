import unittest
from random import shuffle


class BubbleSortTest(unittest.TestCase):
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

    def test_shuffled_4000(self):
        items = list(range(4000))
        shuffle(items)
        self.do_test(items)

    def test_ordered_4000(self):
        items = list(range(4000))
        self.do_test(items)

    def test_reversed_4000(self):
        items = list(reversed(range(4000)))
        self.do_test(items)

    def do_test(self, items: list[int]):
        expected = list(sorted(items))
        bubble_sort(items)
        self.assertListEqual(expected, items)


def bubble_sort(items: list[int]):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(items) - 1):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                is_sorted = False
        # ?? back to while


"""
is_sorted = True
5 4 3 2 1
    (5 4): swap, is_sorted = False
    4 5 3 2 1
    (5 3): swap
    4 3 5 2 1
    (5 2): swap
    4 3 2 5 1
    (5 1): swap
    4 3 2 1 5
is_sorted = True
4 3 2 1 5
    (4 3): swap, is_sorted = False
    3 4 2 1 5
    (4 2): swap
    3 2 4 1 5
    (4 1): swap
    3 2 1 4 5
    (4 5): no swap
    3 2 1 4 5
is_sorted = True
3 2 1 4 5
    is_sorted = False
    2 swaps
    2 1 3 4 5
is_sorted = True
2 1 3 4 5
    is_sorted = False
    1 swap
    1 2 3 4 5
is_sorted = True
1 2 3 4 5
    no swaps
done!

operations(reversed list size n) = sum(k from 0 to n - 1) = n * (n - 1) / 2
O(n^2)

"""

if __name__ == "__main__":
    unittest.main()
