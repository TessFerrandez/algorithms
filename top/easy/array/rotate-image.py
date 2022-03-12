from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def flipdiag(matrix, rows, cols):
            for r in range(1, rows):
                for c in range(r):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        def fliplr(matrix, rows, cols):
            for r in range(rows):
                for c in range(cols // 2):
                    matrix[r][c], matrix[r][cols - c - 1] = matrix[r][cols - c - 1], matrix[r][c]

        rows, cols = len(matrix), len(matrix[0])
        flipdiag(matrix, rows, cols)
        fliplr(matrix, rows, cols)


solution = Solution()

image = [[1,2,3],[4,5,6],[7,8,9]]
solution.rotate(image)
assert image == [[7,4,1],[8,5,2],[9,6,3]]

image = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
solution.rotate(image)
assert image == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
