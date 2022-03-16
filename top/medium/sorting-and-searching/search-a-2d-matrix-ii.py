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
