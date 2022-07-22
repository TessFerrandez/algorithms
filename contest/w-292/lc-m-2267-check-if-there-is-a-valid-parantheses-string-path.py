from collections import defaultdict
from typing import List


class Solution:
    def hasValidPath1(self, grid: List[List[str]]) -> bool:
        if grid[0][0] == ')':
            return False

        dp = defaultdict(set)
        dp[(0, 0)].add(1)
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                to_open = 1 if grid[row][col] == '(' else -1
                for open in dp[(row - 1, col)]:
                    if open + to_open >= 0:
                        dp[(row, col)].add(open + to_open)
                for open in dp[(row, col - 1)]:
                    if open + to_open >= 0:
                        dp[(row, col)].add(open + to_open)

        return 0 in dp[(rows - 1, cols - 1)]

    # cleaner
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        dp = defaultdict(set)

        dp[0, -1] = dp[-1, 0] = {0}

        for row in range(rows):
            for col in range(cols):
                to_open = 1 if grid[row][col] == '(' else -1
                dp[row, col] |= {open + to_open for open in dp[row - 1, col] | dp[row, col - 1] if open + to_open >= 0}

        return 0 in dp[rows - 1, cols - 1]


solution = Solution()
assert not solution.hasValidPath([[")",")"],["(","("]])
assert solution.hasValidPath([["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]])
assert not solution.hasValidPath([["(",")"],["(",")"]])
