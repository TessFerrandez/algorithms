from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = cols = len(matrix)

        for r in range(1, rows):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for r in range(rows):
            for c in range(cols // 2):
                matrix[r][c], matrix[r][cols - c - 1] = matrix[r][cols - c - 1], matrix[r][c]


solution = Solution()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution.rotate(matrix)
assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
