from collections import defaultdict


class Solution:
    def uniquePaths(self, rows: int, cols: int) -> int:
        paths = defaultdict(int)
        paths[(rows - 1, cols - 1)] = 1

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if row == rows - 1 and col == cols - 1:
                    continue
                paths[(row, col)] = paths[(row + 1, col)] + paths[(row, col + 1)]

        return paths[(0, 0)]


solution = Solution()
assert solution.uniquePaths(3, 7) == 28
assert solution.uniquePaths(3, 2) == 3
