from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows_to_zero, cols_to_zero = set(), set()

        for r, row in enumerate(matrix):
            for c, num in enumerate(row):
                if num == 0:
                    rows_to_zero.add(r)
                    cols_to_zero.add(c)

        for row in rows_to_zero:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0

        for col in cols_to_zero:
            for row in range(len(matrix)):
                matrix[row][col] = 0


solution = Solution()

matrix = [[1,1,1],[1,0,1],[1,1,1]]
solution.setZeroes(matrix)
assert matrix == [[1,0,1],[0,0,0],[1,0,1]]

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
solution.setZeroes(matrix)
assert matrix == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
