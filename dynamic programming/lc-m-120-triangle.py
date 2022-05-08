'''
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example
--------------
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:

   2
  3 4
 6 5 7
4 1 8 3

The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
'''
from functools import cache
from typing import List


class Solution:
    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        # for each num in current row - min value is current_val + min(i, i + 1) in next row
        dp = [0 for _ in range(len(triangle) + 1)]

        while triangle:
            current_row = triangle.pop()
            for i, num in enumerate(current_row):
                dp[i] = num + min(dp[i], dp[i + 1])

        return dp[0]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)

        @cache
        def min_path(row, col):
            if row == rows - 1:
                return triangle[row][col]
            return triangle[row][col] + min(min_path(row + 1, col), min_path(row + 1, col + 1))

        return min_path(0, 0)


solution = Solution()
assert solution.minimumTotal([[2], [3, 4],[6, 5, 7],[4, 1, 8, 3]]) == 11
assert solution.minimumTotal([[-10]]) == -10
