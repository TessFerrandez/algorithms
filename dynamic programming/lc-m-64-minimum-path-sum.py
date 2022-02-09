'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        dp[0][0] = grid[0][0]

        for col in range(1, cols):
            dp[0][col] = grid[0][col] + dp[0][col - 1]

        for row in range(1, rows):
            dp[row][0] = grid[row][0] + dp[row - 1][0]

        for row in range(1, rows):
            for col in range(1, cols):
                dp[row][col] = grid[row][col] + min(dp[row - 1][col], dp[row][col - 1])

        return dp[rows - 1][cols - 1]


solution = Solution()

assert solution.minPathSum([[7, 4, 8, 7, 9, 3, 7, 5, 0], [1, 8, 2, 2, 7, 1, 4, 5, 7], [4, 6, 4, 7, 7, 4, 8, 2, 1], [1, 9, 6, 9, 8, 2, 9, 7, 2], [5, 5, 7, 5, 8, 7, 9, 1, 4], [0, 7, 9, 9, 1, 5, 3, 9, 4]]) == 50
assert solution.minPathSum([[1, 2], [5, 6], [1, 1]]) == 8
assert solution.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
assert solution.minPathSum([[1, 2, 3], [4, 5, 6]]) == 12
