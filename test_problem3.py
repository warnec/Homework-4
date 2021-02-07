import unittest
from problem3 import combineStrings


class TestCase(unittest.TestCase):

    def test_Str1(self):
        self.assertEqual(combineStrings("test","ing"), "testing")
    def test_Str2(self):
        self.assertEqual(combineStrings("test", 0), None)
    def test_Str3(self):
        self.assertEqual(combineStrings("test",""), None)

if __name__ == '__main__':
    unittest.main(verbosity=2)