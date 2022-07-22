from collections import defaultdict
from functools import cache


class Solution:
    # tle - brute force
    def findPaths1(self, rows: int, cols: int, maxMove: int, startRow: int, startColumn: int) -> int:
        exits = defaultdict(int)
        for row in range(rows):
            exits[(row, 0)] += 1
            exits[(row, cols - 1)] += 1
        for col in range(cols):
            exits[(0, col)] += 1
            exits[(rows - 1, col)] += 1

        current_positions = [(startRow, startColumn)]
        total_exits = 0

        for _ in range(maxMove):
            next_positions = []
            for r, c in current_positions:
                total_exits += exits[(r, c)]
                for nr, nc in (r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1):
                    if 0 <= nr < rows and 0 <= nc < cols:
                        next_positions.append((nr, nc))
            current_positions = next_positions

        return total_exits % (10 ** 9 + 7)

    # dp with memoization
    def findPaths2(self, rows: int, cols: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def paths(moves_left, row, col):
            if row == rows or col == cols or row < 0 or col < 0:
                return 1
            if moves_left == 0:
                return 0
            total_paths = paths(moves_left - 1, row - 1, col) + paths(moves_left - 1, row + 1, col) + paths(moves_left - 1, row, col + 1) + paths(moves_left - 1, row, col - 1)
            return total_paths

        return paths(maxMove, startRow, startColumn) % (10 ** 9 + 7)

    # dp
    def findPaths(self, rows: int, cols: int, maxMove: int, startRow: int, startColumn: int) -> int:
        modulo = 10 ** 9 + 7
        dp = defaultdict(int)
        dp[(startRow, startColumn)] = 1
        count = 0

        for _ in range(maxMove):
            temp = defaultdict(int)
            for row in range(rows):
                for col in range(cols):
                    if row == rows - 1:
                        count = (count + dp[(row, col)]) % modulo
                    if col == cols - 1:
                        count = (count + dp[(row, col)]) % modulo
                    if row == 0:
                        count = (count + dp[(row, col)]) % modulo
                    if col == 0:
                        count = (count + dp[(row, col)]) % modulo
                    temp[(row, col)] = (dp[(row - 1, col)] + dp[(row + 1, col)] + dp[(row, col - 1)] + dp[(row, col + 1)]) % modulo
            dp = temp

        return count


solution = Solution()
assert solution.findPaths(1, 3, 3, 0, 1) == 12
assert solution.findPaths(2, 2, 2, 0, 0) == 6
