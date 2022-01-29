'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''
from typing import List
from collections import Counter


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_valid(arr):
            counts = Counter(arr)
            del counts['.']
            if not counts.values():
                return True
            return max(counts.values()) <= 1

        # validate all rows
        for row in board:
            if not is_valid(row):
                return False

        # validate all columns
        for col in range(9):
            column = [row[col] for row in board]
            if not is_valid(column):
                return False

        # validate boxes
        for box_r in range(3):
            for box_c in range(3):
                box = []
                for r in range(box_r * 3, box_r * 3 + 3):
                    box += board[r][box_c * 3: box_c * 3 + 3]
                if not is_valid(box):
                    return False

        return True


solution = Solution()

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
assert solution.isValidSudoku(board)

board = [["8","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
assert not solution.isValidSudoku(board)
