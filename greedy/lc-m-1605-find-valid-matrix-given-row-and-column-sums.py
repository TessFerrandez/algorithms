'''
You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.
'''
from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows, cols = len(rowSum), len(colSum)
        matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                val = min(rowSum[row], colSum[col])
                matrix[row][col] = val
                rowSum[row] -= val
                colSum[col] -= val

        return matrix


solution = Solution()
assert solution.restoreMatrix([3, 8], [4, 7]) == [[3, 0], [1, 7]]
assert solution.restoreMatrix([5, 7, 10], [8, 6, 8]) == [[5, 0, 0], [3, 4, 0], [0, 2, 8]]
