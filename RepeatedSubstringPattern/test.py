import unittest
from repeated_substring_pattern import RepeatedSubstringPattern

class TestRepeatedSubstringPattern(unittest.TestCase):
    def test1(self):
        obj = RepeatedSubstringPattern()
        solution = obj.repeatedSubstringPattern("ababab")
        self.assertEqual(solution, True)
        
    def test2(self):
        obj = RepeatedSubstringPattern()
        solution = obj.repeatedSubstringPattern('aba')
        self.assertEqual(solution, False)
        
    def test3(self):
        obj = RepeatedSubstringPattern()
        solution = obj.repeatedSubstringPattern('abcabcabcabc')
        self.assertEqual(solution, True)
        
    def test4(self):
        obj = RepeatedSubstringPattern()
        solution = obj.repeatedSubstringPattern('abac')
        self.assertEqual(solution, False)
    
    def test5(self):
        obj = RepeatedSubstringPattern()
        solution = obj.repeatedSubstringPattern("babbabbabbabbab")
        self.assertEqual(solution, True)
        
if __name__ == '__main__':
    unittest.main()