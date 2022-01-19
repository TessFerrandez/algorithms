'''
Back-tracking

solve the soduku board in place
'''
from typing import List
from itertools import product

SHAPE = 9
GRID = 3
EMPTY = '.'
DIGITS = set([str(num) for num in range(1, SHAPE + 1)])


def get_rows(board):
    for row in range(SHAPE):
        yield board[row]


def get_columns(board):
    for col in range(SHAPE):
        column = [board[row][col] for row in range(SHAPE)]
        yield column


def get_nth_row(board, n):
    return board[n]


def get_nth_col(board, n):
    return [board[row][n] for row in range(SHAPE)]


def get_box_at_row_col(board, row, col):
    row = row // GRID * GRID
    col = col // GRID * GRID
    return [board[r][c] for r, c in product(range(row, row + GRID), range(col, col + GRID))]


def get_boxes(board):
    for row in range(0, SHAPE, GRID):
        for col in range(0, SHAPE, GRID):
            grid = [board[r][c] for r, c in
                    product(range(row, row + GRID), range(col, col + GRID))]
            yield grid


def is_valid_state(board):
    # validate rows
    for row in get_rows(board):
        if not set(row) == DIGITS:
            return False

    # validate columns
    for col in get_columns(board):
        if not set(col) == DIGITS:
            return False

    # validate sub-boxes
    for box in get_boxes(board):
        if not set(box) == DIGITS:
            return False

    return True


def get_candidates(board, row, col):
    used_digits = set()

    # remove digits used by the same row
    used_digits.update(get_nth_row(board, row))

    # remove digits used by the same column
    used_digits.update(get_nth_col(board, col))

    # remove digits used by the sub-box
    used_digits.update(get_box_at_row_col(board, row, col))

    # we may have added the empty string
    used_digits -= set([EMPTY])

    candidates = DIGITS - used_digits
    return candidates


def search(board) -> bool:
    if is_valid_state(board):
        return True # found solution

    for row_idx, row in enumerate(board):
        for col_idx, elm in enumerate(row):
            if elm == EMPTY:
                # find candidates to construct next state
                for candidate in get_candidates(board, row_idx, col_idx):
                    board[row_idx][col_idx] = candidate
                    # recurse on the modified board
                    is_solved = search(board)
                    if is_solved:
                        return True
                    else:
                        # undo the wrong gess
                        board[row_idx][col_idx] = EMPTY
                # exhaussted all candidates
                # but none solved the problem
                return False

    # no empty spot
    return True


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        search(board)


solution = Solution()

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solution.solveSudoku(board)
assert board == [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
