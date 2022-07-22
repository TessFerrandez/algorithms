from collections import defaultdict
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])

        for row in matrix:
            for col in range(cols - 1):
                row[col + 1] += row[col]

        result = 0
        for col in range(cols):
            for col2 in range(col, cols):
                counts = defaultdict(int)
                current, counts[0] = 0, 1
                for row in range(rows):
                    current += matrix[row][col2] - (matrix[row][col - 1] if col > 0 else 0)
                    result += counts[current - target]
                    counts[current] += 1

        return result


solution = Solution()
assert solution.numSubmatrixSumTarget([[0,1,0],[1,1,1],[0,1,0]], 0) == 4
assert solution.numSubmatrixSumTarget([[1,-1],[-1,1]], 0) == 5
assert solution.numSubmatrixSumTarget([[904]], 0) == 0
