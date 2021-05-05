import unittest

from hackerrank import finding_the_percentage


class Tests(unittest.TestCase):
    def test_sample_0(self):
        marks = {
            "Krishna": [67, 68, 69],
            "Arjun": [70, 98, 63],
            "Malika": [52, 56, 60],
        }
        query = "Malika"
        expected = 56.0
        actual = finding_the_percentage.percentage(marks, query)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
