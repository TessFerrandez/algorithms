from bisect import bisect_left
from collections import defaultdict
from typing import List


class Solution:
    # my contest solution - with binary search
    def countUnguarded1(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        rows = defaultdict(list)
        cols = defaultdict(list)
        blocks = guards + walls
        blocks.sort()

        guarded = set()
        for r, c in blocks:
            rows[r].append(c)
            cols[c].append(r)
            guarded.add((r, c))

        for r, c in guards:
            i = bisect_left(rows[r], c)
            left = 0 if i == 0 else rows[r][i - 1] + 1
            for col in range(left, rows[r][i]):
                guarded.add((r, col))
            right = n if i == (len(rows[r]) - 1) else rows[r][i + 1]
            for col in range(rows[r][i] + 1, right):
                guarded.add((r, col))

            i = bisect_left(cols[c], r)
            up = 0 if i == 0 else cols[c][i - 1] + 1
            for row in range(up, cols[c][i]):
                guarded.add((row, c))
            down = m if i == (len(cols[c]) - 1) else cols[c][i + 1]
            for row in range(cols[c][i] + 1, down):
                guarded.add((row, c))

        return m * n - len(guarded)

    # simple dp
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        dp = [[0] * n for _ in range(m)]
        for row, col in guards + walls:
            dp[row][col] = 1

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for row, col in guards:
            for dr, dc in directions:
                curr_row = row
                curr_col = col

                while 0 <= curr_row + dr < m and 0 <= curr_col + dc < n and dp[curr_row + dr][curr_col + dc] != 1:
                    curr_row += dr
                    curr_col += dc
                    dp[curr_row][curr_col] = 2

        return sum(1 for row in range(m) for col in range(n) if dp[row][col] == 0)


solution = Solution()
assert solution.countUnguarded(4, 6, [[0,0],[1,1],[2,3]], [[0,1],[2,2],[1,4]]) == 7
assert solution.countUnguarded(3, 3, [[1,1]], [[0,1],[1,0],[2,1],[1,2]]) == 4
