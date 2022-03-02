'''
You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.
'''
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                grid[row][col] = 0
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)

        # block out the open islands
        for row in range(rows):
            if grid[row][0] == 1:
                dfs(row, 0)
            if grid[row][cols - 1] == 1:
                dfs(row, cols - 1)

        for col in range(cols):
            if grid[0][col] == 1:
                dfs(0, col)
            if grid[rows - 1][col] == 1:
                dfs(rows - 1, col)

        # count the enclaves
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    count += 1

        return count


solution = Solution()
assert solution.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]) == 3
assert solution.numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]) == 0
