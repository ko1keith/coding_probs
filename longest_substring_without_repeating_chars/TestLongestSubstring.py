import unittest
from LongestSubstring import LongestSubstring


class TestLongestSubstring(unittest.TestCase):
    def test_longest_substring(self):
        obj = LongestSubstring()
        length_1 = obj.longest_substring("")
        self.assertEqual(length_1, 0)

        length_2 = obj.longest_substring("hello")
        self.assertEqual(length_2, 3)


if __name__ == "__main__":
    unittest.main()