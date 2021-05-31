import unittest
from hackerrank.interviewprep.arrays import left_rotation


class LeftRotationTestCase(unittest.TestCase):
    def test_d_0(self):
        self.assertEqual([1, 2, 3, 4, 5], left_rotation.rotLeft([1, 2, 3, 4, 5], 0))

    def test_d_3(self):
        self.assertEqual([4, 5, 1, 2, 3], left_rotation.rotLeft([1, 2, 3, 4, 5], 3))


if __name__ == "__main__":
    unittest.main()
