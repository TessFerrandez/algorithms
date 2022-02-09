'''
Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

i - k <= r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix.
'''
from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.rows, self.cols = len(matrix), len(matrix[0])
        self.range_sum = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        for row in range(self.rows):
            for col in range(self.cols):
                self.range_sum[row + 1][col + 1] = self.range_sum[row + 1][col] + self.range_sum[row][col + 1] - self.range_sum[row][col] + matrix[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, r2, c1, c2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1
        full = self.range_sum[r2][c2]
        top = self.range_sum[r1 - 1][c2]
        left = self.range_sum[r2][c1 - 1]
        top_left = self.range_sum[r1 - 1][c1 - 1]
        return  full - top - left + top_left


mat = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
print(mat.sumRegion(2, 1, 4, 3))
