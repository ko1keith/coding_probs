import unittest
from longest_common_prefix import LongestCommonPrefix

class TestLongestCommonPrefix(unittest.TestCase):
    
    def test_1(self):
        obj = LongestCommonPrefix()
        solution = obj.longestCommonPrefix(["flower","flow","flight"])
        self.assertEquals(solution, "fl")
        
    def test_2(self):
        obj = LongestCommonPrefix()
        solution = obj.longestCommonPrefix(["dog","racecar","car"])
        self.assertEquals(solution, "")

    def test_3(self):
        obj = LongestCommonPrefix()
        solution = obj.longestCommonPrefix(["cir","car"])
        self.assertEquals(solution, "c")
        
if __name__ == "__main__":
    unittest.main()