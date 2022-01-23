from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        h, w = len(mat), len(mat[0])

        if h == 0 or w == 0:
            return []

        for row in range(h - 1, -1, -1):
            diag_nums = []
            r, c = row, 0
            while r < h and c < w:
                diag_nums.append(mat[r][c])
                r += 1
                c += 1
            diag_nums.sort()
            r, c, i = row, 0, 0
            while r < h and c < w:
                mat[r][c] = diag_nums[i]
                r += 1
                c += 1
                i += 1

        if h == 1:
            return mat

        for col in range(1, w):
            diag_nums = []
            r, c = 0, col
            while c < w and r < h:
                diag_nums.append(mat[r][c])
                r += 1
                c += 1
            diag_nums.sort()
            r, c, i = 0, col, 0
            while c < w and r < h:
                mat[r][c] = diag_nums[i]
                r += 1
                c += 1
                i += 1

        return mat


solution = Solution()
assert solution.diagonalSort([[75,21,13,24,8],[24,100,40,49,62]]) == [[75, 21, 13, 24, 8], [24, 100, 40, 49, 62]]
assert solution.diagonalSort([[37,98,82,45,42]]) == [[37,98,82,45,42]]
assert solution.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]) == [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
assert solution.diagonalSort([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]) == [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]
