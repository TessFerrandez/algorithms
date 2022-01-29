'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
'''
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        result = [1]
        prev_row = self.getRow(rowIndex - 1)
        for i in range(1, rowIndex):
            result.append(prev_row[i - 1] + prev_row[i])
        result.append(1)

        return result


solution = Solution()
assert solution.getRow(3) == [1, 3, 3, 1]
assert solution.getRow(0) == [1]
assert solution.getRow(1) == [1, 1]
