'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
'''
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])

        def target_in_row(row: List[int]) -> bool:
            low, high = 0, n - 1

            while low <= high:
                mid = (low + high) // 2
                if row[mid] == target:
                    return True
                elif row[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1

            return False

        for row in matrix:
            if row[0] <= target <= row[n - 1]:
                if target_in_row(row):
                    return True
            if row[0] > target:
                break
        return False


solution = Solution()
assert solution.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5)
assert not solution.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20)
