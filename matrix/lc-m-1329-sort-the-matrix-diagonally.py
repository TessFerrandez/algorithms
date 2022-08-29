from collections import defaultdict
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])

        diags = defaultdict(list)

        for row in range(rows):
            for col in range(cols):
                diags[row - col].append(mat[row][col])

        for diag in diags:
            diags[diag].sort(reverse=1)

        for row in range(rows):
            for col in range(cols):
                mat[row][col] = diags[row - col].pop()

        return mat


solution = Solution()
assert solution.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]) == [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
assert solution.diagonalSort([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]) == [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
