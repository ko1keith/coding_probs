import unittest
from implement_str_str import ImplementStrStr

class TestImplementStrStr(unittest.TestCase):
    def test1(self):
        obj = ImplementStrStr()
        solution = obj.strStr("hello", "ll")
        self.assertEqual(solution, 2)
    
    def test2(self):
        obj = ImplementStrStr()
        solution = obj.strStr("aaaaa", "bba")
        self.assertEqual(solution, -1)
        
    def test3(self):
        obj = ImplementStrStr()
        solution = obj.strStr("aaaaa", "")
        self.assertEqual(solution, 0)
        
    def test4(self):
        obj = ImplementStrStr()
        solution = obj.strStr("aaaap", "ap")
        self.assertEqual(solution, 3)
    
    def test5(self):
        obj = ImplementStrStr()
        solution = obj.strStr("a", "a")
        self.assertEqual(solution, 0)
        
    def test6(self):
        obj = ImplementStrStr()
        solution = obj.strStr("abc", "c")
        self.assertEqual(solution, 2)
        
        
        
if __name__ == "__main__":
    unittest.main()