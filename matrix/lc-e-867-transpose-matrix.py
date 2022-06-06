from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        result = [[0 for _ in range(rows)] for _ in range(cols)]

        for row in range(rows):
            for col in range(cols):
                result[col][row] = matrix[row][col]

        return result


solution = Solution()
assert solution.transpose([[1,2,3],[4,5,6],[7,8,9]]) == [[1,4,7],[2,5,8],[3,6,9]]
assert solution.transpose([[1,2,3],[4,5,6]]) == [[1,4],[2,5],[3,6]]
