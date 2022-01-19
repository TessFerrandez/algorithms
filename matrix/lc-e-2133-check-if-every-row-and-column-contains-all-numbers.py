'''
An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.
'''
from typing import List
from collections import defaultdict


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)

        for row in matrix:
            freq = defaultdict(int)
            for num in row:
                if num in freq:
                    return False
                else:
                    freq[num] = 1

        for col in range(n):
            freq = defaultdict(int)
            for row in range(n):
                if matrix[row][col] in freq:
                    return False
                else:
                    freq[matrix[row][col]] = 1

        return True


solution = Solution()
assert solution.checkValid([[2,2,2],[2,2,2],[2,2,2]]) == False
assert solution.checkValid([[1,2,3],[3,1,2],[2,3,1]]) == True
assert solution.checkValid([[1,1,1],[1,2,3],[1,2,3]]) == False