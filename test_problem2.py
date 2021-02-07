import unittest
from problem2 import listAvg


class TestCase(unittest.TestCase):

    def test_avg1(self):
        self.assertEqual(listAvg([1,1,1,1,1]), 1.0)
    def test_avg2(self):
        self.assertEqual(listAvg([-1,-1,1,1]), None)
    def test_avg3(self):
        self.assertEqual(listAvg([]), None)

if __name__ == '__main__':
    unittest.main(verbosity=2)