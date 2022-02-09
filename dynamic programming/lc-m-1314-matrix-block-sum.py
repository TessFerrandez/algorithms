'''
Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

i - k <= r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix.
'''
from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        range_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        for row in range(rows):
            for col in range(cols):
                range_sum[row + 1][col + 1] = range_sum[row + 1][col] + range_sum[row][col + 1] - range_sum[row][col] + mat[row][col]

        max_sums = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                r1, c1, r2, c2 = max(0, row - k), max(0, col - k), min(rows, row + k + 1), min(cols, col + k + 1)
                max_sums[row][col] = range_sum[r2][c2] - range_sum[r1][c2] - range_sum[r2][c1] + range_sum[r1][c1]
        return max_sums


solution = Solution()
assert solution.matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1) == [[12, 21, 16], [27, 45, 33], [24, 39, 28]]
