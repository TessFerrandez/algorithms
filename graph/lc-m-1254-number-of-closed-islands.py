'''
Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.
'''
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 0:
                grid[row][col] = 1
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)

        # block out the open islands
        for row in range(rows):
            if grid[row][0] == 0:
                dfs(row, 0)
            if grid[row][cols - 1] == 0:
                dfs(row, cols - 1)

        for col in range(cols):
            if grid[0][col] == 0:
                dfs(0, col)
            if grid[rows - 1][col] == 0:
                dfs(rows - 1, col)

        # count the closed islands
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    if not dfs(row, col):
                        count += 1

        return count


solution = Solution()
assert solution.closedIsland([[0,0,1,1,0,1,0,0,1,0],
                              [1,1,0,1,1,0,1,1,1,0],
                              [1,0,1,1,1,0,0,1,1,0],
                              [0,1,1,0,0,0,0,1,0,1],
                              [0,0,0,0,0,0,1,1,1,0],
                              [0,1,0,1,0,1,0,1,1,1],
                              [1,0,1,0,1,1,0,0,0,1],
                              [1,1,1,1,1,1,0,0,0,0],
                              [1,1,1,0,0,1,0,1,0,1],
                              [1,1,1,0,1,1,0,1,1,0]]) == 5
assert solution.closedIsland([[1,1,1,1,1,1,1,0],
                              [1,0,0,0,0,1,1,0],
                              [1,0,1,0,1,1,1,0],
                              [1,0,0,0,0,1,0,1],
                              [1,1,1,1,1,1,1,0]]) == 2
assert solution.closedIsland([[0,0,1,0,0],
                              [0,1,0,1,0],
                              [0,1,1,1,0]]) == 1
