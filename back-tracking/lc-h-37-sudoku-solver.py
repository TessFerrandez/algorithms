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


def solve_sudoku(board: List[List[str]]):
    search(board)


def parse_board(string_board) -> List[List[str]]:
    return [list(row) for row in string_board.splitlines()]


string_board = '''53..7....
6..195...
.98....6.
8...6...3
4..8.3..1
7...2...6
.6....28.
...419..5
....8..79
'''

board = parse_board(string_board)
solve_sudoku(board)

for row in board:
    print(''.join(row))
