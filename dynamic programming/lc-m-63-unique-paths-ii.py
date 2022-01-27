'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.
'''
from typing import List
from collections import defaultdict


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        paths_from = defaultdict(int)

        if not obstacleGrid:
            return 0

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[rows - 1][cols - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if row == rows - 1 and col == cols - 1:
                    paths_from[(col, row)] = 1
                else:
                    down = 0 if (row + 1 == rows or obstacleGrid[row + 1][col] == 1) else paths_from[(col, row + 1)]
                    right = 0 if (col + 1 == cols or obstacleGrid[row][col + 1] == 1) else paths_from[(col + 1, row)]
                    paths_from[(col, row)] = down + right

        return paths_from[(0, 0)]


solution = Solution()
assert solution.uniquePathsWithObstacles([[1, 0]]) == 0
assert solution.uniquePathsWithObstacles([]) == 0
assert solution.uniquePathsWithObstacles([[1]]) == 0
assert solution.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
assert solution.uniquePathsWithObstacles([[0, 1], [0, 0]]) == 1
