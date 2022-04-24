from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(row, target):
            low, high = 0, len(row) - 1

            while low <= high:
                mid = (low + high) // 2
                if row[mid] == target:
                    return True
                if row[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

            return False

        def find_row():
            low, high = 0, len(matrix) - 1
            while low < high:
                mid = (low + high) // 2
                if matrix[mid][0] <= target and matrix[mid + 1][0] > target:
                    return mid
                if matrix[mid][0] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return low

        row = find_row()
        return search(matrix[row], target)


solution = Solution()
assert solution.searchMatrix([[1]], 1)
assert solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)
assert not solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)
