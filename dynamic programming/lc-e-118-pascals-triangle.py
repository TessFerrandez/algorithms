'''
Given an integer numRows, return the first numRows of Pascal's triangle.
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for row in range(1, numRows):
            result.append([1])
            prev_row = row - 1
            for i in range(1, row):
                result[row].append(result[prev_row][i - 1] + result[prev_row][i])
            result[row].append(1)

        return result


solution = Solution()
assert solution.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
