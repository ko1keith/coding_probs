import unittest
from palindrome_number import PalindromeNumber
class TestPalindromNumber(unittest.TestCase):
    def setUp(self):
        self.int_1 = 121
        self.output_expected_1 = True
        
        self.int_2 = -121
        self.output_expected_2 = False
        
        self.int_3 = 10
        self.output_expected_3 = False
        
    def test_1(self):
        obj = PalindromeNumber()
        solution = obj.isPalindrome(self.int_1)
        self.assertEqual(solution, self.output_expected_1)
        
    def test_2(self):
        obj = PalindromeNumber()
        solution = obj.isPalindrome(self.int_2)
        self.assertEqual(solution, self.output_expected_2)

    def test_3(self):
        obj = PalindromeNumber()
        solution = obj.isPalindrome(self.int_3)
        self.assertEqual(solution, self.output_expected_3)
        
if __name__ == '__main__':
    unittest.main()
    