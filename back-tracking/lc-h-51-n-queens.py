'''
Back tracking

place n queens on a board such that they
don't attack eachother

return all possible solutions

ex. input 4
output = [['.Q..', '...Q', 'Q...', '..Q.'],
          ['..Q.', 'Q...', '...Q', '.Q..']]

We can store these two output states as
         [[1, 3, 0, 2], [2, 0, 3, 1]]
'''
from typing import List


def is_valid_state(state, n):
    return len(state) == n


def get_candidates(state, n):
    if not state:
        # all positions on row are possible
        return range(n)

    # find the next position (row) to populate
    position = len(state)

    # start with all columns
    candidates = set(range(n))

    # prune down candidates that place queens in attacks
    for row, col in enumerate(state):
        # discard the column index if it's occupied by a queen
        candidates.discard(col)

        # discard diagonals
        dist = position - row
        candidates.discard(col + dist)
        candidates.discard(col - dist)

    return candidates


def search(state, solutions, n):
    if is_valid_state(state, n):
        solutions.append(state.copy())
        return  # we only want one solution

    for candidate in get_candidates(state, n):
        state.append(candidate)
        search(state, solutions, n)
        state.pop()


def state_to_strings(state, n):
    # ex [1, 3, 0, 2] = [".Q..", "...Q", "Q...", "..Q."]
    result = []

    for i in state:
        string = '.' * i + 'Q' + '.' * (n - i - 1)
        result.append(string)

    return result


def solve_queens(n: int) -> List[List[str]]:
    solutions, state = [], []
    search(state, solutions, n)
    return [state_to_strings(state, n) for state in solutions]


print(solve_queens(4))
