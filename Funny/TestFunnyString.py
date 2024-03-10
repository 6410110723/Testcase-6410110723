import unittest
from FunnyString import Funny  

class TestFunnyString(unittest.TestCase):

    def test_funny_string(self):
        self.assertEqual(Funny("acxz"), "Funny")

    def test_not_funny_string(self):
        self.assertEqual(Funny("bcxz"), "Not Funny")

    def test_funny_string_with_repeated_characters(self):
        self.assertEqual(Funny("level"), "Funny")

    def test_funny_string_single_character(self):
        self.assertEqual(Funny("o"), "Funny")  

    def test_funny_string_empty(self):
        self.assertEqual(Funny(""), "Funny")

if __name__ == '__main__':
    unittest.main()