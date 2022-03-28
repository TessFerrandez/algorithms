import numpy as np
from typing import List


class Solution:
    # easy version
    def gameOfLife1(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])
        nboard = np.array(board)

        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                rmin, rmax = max(0, r - 1), min(r + 1, rows - 1)
                cmin, cmax = max(0, c - 1), min(c + 1, cols - 1)
                neighbors = nboard[rmin: rmax + 1, cmin: cmax + 1].sum()

                if cell == 1 and neighbors not in (3, 4):
                    board[r][c] = 0
                if cell == 0 and neighbors == 3:
                    board[r][c] = 1

    # in place
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows, cols = len(board), len(board[0])

        if rows == 0 or cols == 0:
            return

        for row in range(rows):
            for col in range(cols):
                neighbors = sum([board[r][c] % 2 for r in range(row - 1, row + 2) for c in range(col - 1, col + 2) if 0 <= r < rows and 0 <= c < cols]) - board[row][col]
                if board[row][col] == 0 and neighbors == 3:
                    board[row][col] = 2
                if board[row][col] == 1 and (neighbors < 2 or neighbors > 3):
                    board[row][col] = 3

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 2:
                    board[row][col] = 1
                if board[row][col] == 3:
                    board[row][col] = 0


solution = Solution()

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
solution.gameOfLife(board)
assert board == [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

board = [[1,1],[1,0]]
solution.gameOfLife(board)
assert board == [[1,1],[1,1]]
