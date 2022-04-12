class Shift2DGrid:
    def shift_2D_grid(self, grid, k):
        if k == 0:
            return grid
        
        flat_grid = []
        m = len(grid)
        n = len(grid[0])
        # flatten grid
        for i in grid:
            for j in i:
                flat_grid.append(j)        

        #shift each element in flat grid by k times
        new_flat = []
        for l in range(k):
            temp_flat = list(new_flat)
            for i in range(len(flat_grid)):
                if i == 0:
                    if l == 0:
                        new_flat.insert(i, flat_grid[len(flat_grid) - 1])
                    else:
                        new_flat[i] = temp_flat[len(temp_flat) - 1]
                else:
                    if l == 0:
                        new_flat.insert(i, flat_grid[i - 1])
                    else:
                        new_flat[i] = temp_flat[i - 1]
        
        #unflatten flat_grid
        new_grid = []
        for i in range(m):
            temp_list = new_flat[(i*n): ((i*n) + n)]
            new_grid.append(temp_list)
                        
        return new_grid