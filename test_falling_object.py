import unittest
from falling_object import calculate_distance


class TestFallingObject(unittest.TestCase):

    def test_two_seconds(self):
        self.assertAlmostEqual(calculate_distance(2), 19.62)

    def test_zero_seconds(self):
        self.assertEqual(calculate_distance(0), 0)

    def test_negative_time(self):
        with self.assertRaises(ValueError):
            calculate_distance(-1)


if __name__ == "__main__":
    unittest.main()
