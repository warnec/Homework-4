import unittest
from problem1 import volume


class TestCase(unittest.TestCase):

    def test_volume(self):
        self.assertEqual(volume(2, 1.6,1), 3.2)
    def test_volume1(self):
        self.assertEqual(volume(0,1,12), None)
    def test_volume2(self):
        self.assertEqual(volume(1,-1,5), None)

if __name__ == '__main__':
    unittest.main(verbosity=2)