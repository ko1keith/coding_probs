import unittest
from merge_two_sorted_lists import MergeTwoSortedLists, ListNode

class TestMergeTwoSortedLists(unittest.TestCase):
    def test_1(self):
        obj = MergeTwoSortedLists()
        solution = obj.merge_two_sorted_lists([1,2,4], [1,3,4])
        self.assertEqual(solution, [1,1,2,3,4,4])


if __name__ == "__main__":
    unittest.main()
