'''
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
'''
from typing import List
from itertools import chain

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        orig_r, orig_c = len(mat), len(mat[0])
        if orig_r * orig_c != r * c:
            return mat

        row = col = 0
        result = []
        for num in chain.from_iterable(mat):
            if col == 0:
                result.append([])

            result[row].append(num)
            if col == c - 1:
                row += 1
                col = 0
            else:
                col += 1

        return result


solution = Solution()
assert solution.matrixReshape([[1, 2], [3, 4]], 1, 4) == [[1, 2, 3, 4]]
assert solution.matrixReshape([[1, 2], [3, 4]], 2, 4) == [[1, 2], [3, 4]]
