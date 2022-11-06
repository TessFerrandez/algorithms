from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        def is_toeplitz_diagonal(row, col):
            number = matrix[row][col]

            while row < rows and col < cols:
                if matrix[row][col] != number:
                    return False
                row += 1
                col += 1

            return True

        for row in range(rows):
            if not is_toeplitz_diagonal(row, 0):
                return False

        for col in range(1, cols):
            if not is_toeplitz_diagonal(0, col):
                return False

        return True


solution = Solution()
assert solution.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]])
assert not solution.isToeplitzMatrix([[1,2],[2,2]])
