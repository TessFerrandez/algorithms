from collections import defaultdict


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths_from = defaultdict(int)

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row == m - 1 or col == n - 1:
                    paths_from[(col, row)] = 1
                else:
                    paths_from[(col, row)] = paths_from[(col, row + 1)] + paths_from[(col + 1, row)]

        return paths_from[(0, 0)]


solution = Solution()
assert solution.uniquePaths(3, 7) == 28
assert solution.uniquePaths(3, 2) == 3
