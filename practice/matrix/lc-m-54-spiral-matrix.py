'''
Given an m x n matrix, return all elements of the matrix in spiral order.
'''
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r, c = len(matrix) - 1, len(matrix[0])

        result = []
        row, col = 0, -1

        vertical = True
        move = 1
        while r >= 0 and c >= 0:
            if vertical:
                for _ in range(c):
                    col += move
                    result.append(matrix[row][col])
                c -= 1
            else:
                for _ in range(r):
                    row += move
                    result.append(matrix[row][col])
                r -= 1
                move = -move
            vertical = not vertical

        return result


solution = Solution()
assert solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
assert solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
