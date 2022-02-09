'''
Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
'''
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)

        prev_sums = matrix[n - 1]

        for row in range(n - 2, -1, -1):
            current_sums = []

            for col in range(n):
                best_sum = min(prev_sums[max(0, col - 1): min(col + 2, n)])
                current_sums.append(matrix[row][col] + best_sum)

            prev_sums = current_sums

        return min(prev_sums)


solution = Solution()
assert solution.minFallingPathSum([[17, 82],[1, -44]]) == -27
assert solution.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]) == 13
assert solution.minFallingPathSum([[-19, 57], [-40, -5]]) == -59
