'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row_low, row_high = 0, len(matrix) - 1
        while row_low < row_high:
            mid = (row_high - row_low) // 2 + row_low
            if matrix[mid][0] > target:
                row_high = mid - 1
            elif matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target and matrix[mid + 1][0] > target:
                row_low, row_high = mid, mid
            else:
                row_low = mid + 1

        row = row_low

        col_low, col_high = 0, len(matrix[0]) - 1
        while col_low <= col_high:
            mid = (col_high - col_low) // 2 + col_low
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                col_low = mid + 1
            else:
                col_high = mid - 1

        return False


solution = Solution()
assert solution.searchMatrix([[1], [3]], 3) == True
assert solution.searchMatrix([[1]], 2) == False
assert solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True
assert solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 16) == True
assert solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False
