import unittest
from TwoSum import TwoSum


class TestPalindrome(unittest.TestCase):

    def test_true_palindrome(self):
        twoSumObj = TwoSum()
        self.assertEqual([2, 3], twoSumObj.twoSum([11, 15, 2, 7], 9))
        self.assertEqual([0, 1], twoSumObj.twoSum([2, 7, 11, 15], 9))


if __name__ == '__main__':
    unittest.main()
