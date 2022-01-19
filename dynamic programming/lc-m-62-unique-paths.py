'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

ALGORITHM
-------------
paths_from(x, y) = paths_from(x + 1, y) + paths_from(x, y + 1)
paths_from(end) = 1

result = paths_from(0, 0)
'''
from collections import defaultdict


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths_from = defaultdict(int)

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row == m - 1 and col == n - 1:
                    paths_from[(col, row)] = 1
                else:
                    paths_from[(col, row)] = paths_from[(col, row + 1)] + paths_from[(col + 1, row)]

        return paths_from[(0, 0)]


solution = Solution()
assert solution.uniquePaths(3, 2) == 3
assert solution.uniquePaths(3, 7) == 28