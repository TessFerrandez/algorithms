from itertools import accumulate
from typing import List
import numpy as np


class Solution:
    # TLE
    def possibleToStamp1(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        matrix = np.array(grid)
        matrix2 = np.copy(matrix)
        for row in range(len(grid) - stampHeight + 1):
            for col in range(len(grid[0]) - stampWidth + 1):
                if not np.any(matrix[row:row + stampHeight, col:col + stampWidth]):
                    matrix2[row:row + stampHeight, col:col + stampWidth] = 2

        return 0 not in matrix2

    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        # preprocessing for 2D range sum query
        def generate_row_col_prefix(grid):
            prefix = [[0] * (len(grid[0]) + 1)]
            for row in grid:
                row = list(accumulate(row, initial=0))
                for col in range(len(row)):
                    row[col] += prefix[-1][col]
                prefix.append(row)
            return prefix

        # query function
        def query_2d_range_sum(prefix, x1, y1, x2, y2):
            return prefix[x2 + 1][y2 + 1] - prefix[x2 + 1][y1] - prefix[x1][y2 + 1] + prefix[x1][y1]

        H, W = len(grid), len(grid[0])
        prefix = generate_row_col_prefix(grid)

        stamp_grid = [[0] * W for _ in range(H)]    # 1 represents valid stamp position
        for row in range(H):
            for col in range(W):
                if row < stampHeight - 1 or col < stampWidth - 1:
                    continue
                else:
                    count = query_2d_range_sum(prefix, row - stampHeight + 1, col - stampWidth + 1, row, col)
                    if count:
                        continue
                    else:
                        stamp_grid[row][col] = 1

        stamp_prefix = generate_row_col_prefix(stamp_grid)
        for row in range(H):
            for col in range(W):
                if grid[row][col] == 1:     # it is occupied at first, ignored
                    continue
                count = query_2d_range_sum(stamp_prefix, row, col, min(row + stampHeight - 1, H - 1), min(col + stampWidth - 1, W - 1))
                if not count:
                    return False
        return True


solution = Solution()
assert solution.possibleToStamp([[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], 4, 3)
assert not solution.possibleToStamp([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], 2, 2)
assert not solution.possibleToStamp([[0,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,1],[0,0,0,1,1]], 2, 2)
