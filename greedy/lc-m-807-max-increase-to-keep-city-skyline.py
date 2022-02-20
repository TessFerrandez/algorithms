'''
There is a city composed of n x n blocks, where each block contains a single building shaped like a vertical square prism. You are given a 0-indexed n x n integer matrix grid where grid[r][c] represents the height of the building located in the block at row r and column c.

A city's skyline is the the outer contour formed by all the building when viewing the side of the city from a distance. The skyline from each cardinal direction north, east, south, and west may be different.

We are allowed to increase the height of any number of buildings by any amount (the amount can be different per building). The height of a 0-height building can also be increased. However, increasing the height of a building should not affect the city's skyline from any cardinal direction.

Return the maximum total sum that the height of the buildings can be increased by without changing the city's skyline from any cardinal direction.
'''
from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_rows = [max(row) for row in grid]

        max_cols = []
        for col in range(cols):
            max_cols.append(max(grid[row][col] for row in range(rows)))

        growth = 0
        for row in range(rows):
            for col in range(cols):
                growth += min(max_rows[row], max_cols[col]) - grid[row][col]

        return growth


solution = Solution()
assert solution.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]) == 35
assert solution.maxIncreaseKeepingSkyline([[0,0,0],[0,0,0],[0,0,0]]) == 0
