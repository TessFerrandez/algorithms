from copy import deepcopy
from typing import List


class Solution:
    '''
    for any given configuration, you can turn one island into two in max 2 days
    ex.
    x x x
    x x x
    x x x
    =>
    x x x
    x x -
    x - x

    Case 1: you have 0 or 2+ islands from start => 0
    Case 2: you have 1 island - try all land locations and see if they give you two islands => 1
    Case 3: all else => return 2
    '''
    def dfs(self, grid, row, col, rows, cols):
        if grid[row][col] == 0:
            return

        grid[row][col] = 0

        if row - 1 >= 0:
            self.dfs(grid, row - 1, col, rows, cols)
        if row + 1 < rows:
            self.dfs(grid, row + 1, col, rows, cols)
        if col - 1 >= 0:
            self.dfs(grid, row, col - 1, rows, cols)
        if col + 1 < cols:
            self.dfs(grid, row, col + 1, rows, cols)

    # find how many islands the given grid has
    def count_islands(self, grid, rows, cols):
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    count += 1
                    self.dfs(grid, row, col, rows, cols)
        return count

    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # if we have 0 or more than 1 islands at day 0, return day 0
        grid_copy = deepcopy(grid)
        if self.count_islands(grid_copy, rows, cols) != 1:
            return 0

        # try to remove any land any see if it works
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue

                grid_copy = deepcopy(grid)
                grid_copy[row][col] = 0
                if self.count_islands(grid_copy, rows, cols) != 1:
                    return 1

        # well then just return 2
        return 2


solution = Solution()
assert solution.minDays([[0,1,1,0],[0,1,1,0],[0,0,0,0]]) == 2
assert solution.minDays([[1,1]]) == 2
