# Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

# In one shift operation:

# Element at grid[i][j] moves to grid[i][j + 1].
# Element at grid[i][n - 1] moves to grid[i + 1][0].
# Element at grid[m - 1][n - 1] moves to grid[0][0].
# Return the 2D grid after applying shift operation k times.

from shift_2d_grid import Shift2DGrid
import unittest

class TestShift2DGrid(unittest.TestCase):
    def setUp(self):
        self.test_1_grid = [[1,2,3],[4,5,6],[7,8,9]]
        self.test_1_k = 1
        self.test_1_expected = [[9,1,2], [3,4,5], [6,7,8]]
        
        self.test_2_grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]]
        self.test_2_k = 4
        self.test_2_expected = [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
        
        self.test_3_grid = [[1,2,3],[4,5,6],[7,8,9]]
        self.test_3_k = 9
        self.test_3_expected = [[1,2,3],[4,5,6],[7,8,9]]
        
        self.test_4_grid = [[1],[2],[3],[4],[7],[6],[5]]
        self.test_4_k = 23
        self.test_4_expected = [[6],[5],[1],[2],[3],[4],[7]]
        

    def test_1(self):    
        obj = Shift2DGrid()
        solution = obj.shift_2D_grid(self.test_1_grid, self.test_1_k)
        self.assertListEqual(self.test_1_expected, solution)
        
    def test_2(self):    
        obj = Shift2DGrid()
        solution = obj.shift_2D_grid(self.test_2_grid, self.test_2_k)
        self.assertListEqual(self.test_2_expected, solution)
    
    def test_3(self):
        obj = Shift2DGrid()
        solution = obj.shift_2D_grid(self.test_3_grid, self.test_3_k)
        self.assertListEqual(self.test_3_expected, solution)
        
    def test_4(self):
        obj = Shift2DGrid()
        solution = obj.shift_2D_grid(self.test_4_grid, self.test_4_k)
        self.assertListEqual(self.test_4_expected, solution)
    



if __name__ == '__main__':
    unittest.main()
    