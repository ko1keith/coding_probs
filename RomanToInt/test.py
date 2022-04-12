import unittest
from roman_to_int import RomanToInt

class TestRomanToInt(unittest.TestCase):
    def setUp(self):
        self.roman_1 = "III"
        self.roman_1_expected = 3
        
        self.roman_2 = "IV"
        self.roman_2_expected = 4
        
        self.roman_3 = "MCMXCIV"
        self.roman_3_expected = 1994
        
        self.obj = RomanToInt()
    
    def test_1(self):
        solution = self.obj.romanToInt(self.roman_1)
        self.assertEqual(solution, self.roman_1_expected)
    
    def test_2(self):
        solution = self.obj.romanToInt(self.roman_2)
        self.assertEqual(solution, self.roman_2_expected)
    
    def test_3(self):
        solution = self.obj.romanToInt(self.roman_3)
        self.assertEqual(solution, self.roman_3_expected)

if __name__ == "__main__":
    unittest.main()