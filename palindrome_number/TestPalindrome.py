import unittest
from Palindrome import Palindrome


class TestPalindrome(unittest.TestCase):

    def test_true_palindrome(self):
        palindromeObj = Palindrome()
        self.assertTrue(palindromeObj.isPalindrome(1))
        self.assertTrue(palindromeObj.isPalindrome(11))
        self.assertTrue(palindromeObj.isPalindrome(101))
        self.assertTrue(palindromeObj.isPalindrome(50005))
        self.assertTrue(palindromeObj.isPalindrome(100010001))

    def test_false_palindrome(self):
        palindromeObj = Palindrome()
        self.assertFalse(palindromeObj.isPalindrome(12))
        self.assertFalse(palindromeObj.isPalindrome(123))
        self.assertFalse(palindromeObj.isPalindrome(123456789))


if __name__ == '__main__':
    unittest.main()
