'''
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
'''
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0

        for i in range(n):
            total += mat[i][i]

        for i in range(n):
            total += mat[i][n - i - 1]

        if n % 2 == 1:
            mid = n // 2
            total -= mat[mid][mid]

        return total


solution = Solution()
assert solution.diagonalSum([[1,2,3], [4,5,6], [7,8,9]]) == 25
assert solution.diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]) == 8
assert solution.diagonalSum([[5]]) == 5
