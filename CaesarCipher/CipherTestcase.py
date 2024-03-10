import unittest
from Cipher import caesar

class TestCaesarCipher(unittest.TestCase):

    def test_lowercase_letters(self):
        self.assertEqual(caesar("abc", 1), "bcd")

    def test_uppercase_letters(self):
        self.assertEqual(caesar("XYZ", 3), "ABC")

    def test_mixed_case_letters(self):
        self.assertEqual(caesar("AbC", 2), "CdE")

    def test_non_alphabetic_characters(self):
        self.assertEqual(caesar("123!@#", 5), "123!@#")

    def test_large_shift_value(self):
        self.assertEqual(caesar("abc", 26), "abc")

    def test_negative_shift_value(self):
        self.assertEqual(caesar("xyz", -3), "uvw")

    def test_large_negative_shift_value(self):
        self.assertEqual(caesar("xyz", -30), "vwx")

if __name__ == '__main__':
    unittest.main()
