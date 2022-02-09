'''
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

DP is 1 based to avoid a bunch of ifs (first row and first col is 0)
DP[i + 1][j + 1] = side of biggest square of ones ending at i, j

Ex.
01110   01110
11110   11220
01111   01231
01111   01232
00111   00123
'''
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i][j], dp[i + 1][j]) + 1
                else:
                    dp[i + 1][j + 1] = 0

        max_side = 0
        for row in range(rows + 1):
            max_side = max(max_side, max(dp[row]))

        return max_side * max_side


solution = Solution()

grid = [["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]]
assert solution.maximalSquare(grid) == 4
