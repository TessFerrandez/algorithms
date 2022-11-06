from functools import cache
from typing import List


class Solution:
    def findBall1(self, grid: List[List[int]]) -> List[int]:
        RIGHT, LEFT = 1, -1

        rows, cols = len(grid), len(grid[0])
        max_row, max_col = rows - 1, cols - 1

        def roll_ball(row, col, top):
            if row == max_row:
                if not top:
                    return col

            if not top:
                return roll_ball(row + 1, col, True)

            if grid[row][col] == RIGHT:
                if col == max_col or grid[row][col + 1] == LEFT:
                    return -1
                else:
                    return roll_ball(row, col + 1, False)
            else:
                if col == 0 or grid[row][col - 1] == RIGHT:
                    return -1
                else:
                    return roll_ball(row, col - 1, False)

        positions = []
        for col in range(cols):
            positions.append(roll_ball(0, col, True))

        return positions

    # dynamic programming
    def findBall2(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        positions = [0] * cols
        cache = {}

        for row in range(rows, -1, -1):
            for col in range(cols):
                if row == rows:
                    cache[(row, col)] = col
                    continue

                next_col = col + grid[row][col]
                if next_col < 0 or next_col >= cols or grid[row][col] != grid[row][next_col]:
                    cache[(row, col)] = -1
                else:
                    cache[(row, col)] = cache[(row + 1, next_col)]

                if row == 0:
                    positions[col] = cache[(row, col)]

        return positions

    # simplified dfs with memo
    def findBall(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])

        @cache
        def roll_ball(row, col):
            if row == rows:
                return col

            next_col = col + grid[row][col]
            if next_col < 0 or next_col >= cols or grid[row][col] != grid[row][next_col]:
                return -1
            return roll_ball(row + 1, next_col)

        return [roll_ball(0, col) for col in range(cols)]


solution = Solution()
assert solution.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]) == [1, -1, -1, -1, -1]
assert solution.findBall([[-1]]) == [-1]
assert solution.findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]) == [0,1,2,3,4,-1]
