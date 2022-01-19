from collections import deque
from typing import Deque, Tuple

'''
Given a chess board, find the minimum number
of moves to move a knight from start to target

See the grid as a graph where the neighbors
are the available moves

We need
1. A way to get neighbors
2. A way to keep track of the number of moves
3. A way to know we hit our target
'''

WIDTH = 5
HEIGHT = 5

MOVES = [2 + 1j, 2 - 1j, -2 + 1j, -2 - 1j, 1 + 2j, 1 - 2j, -1 + 2j, -1 - 2j]


def in_grid(pos):
    x, y = int(pos.real), int(pos.imag)
    return 0 <= y < HEIGHT and 0 <= x < WIDTH


def get_neighbors(pos):
    return [pos + move for move in MOVES if in_grid(pos + move)]


def find_minimum_number_of_moves(start, target):
    visited = set([start])
    todo: Deque[Tuple[complex, int]] = deque([(start, 0)])

    while todo:
        pos, count = todo.popleft()
        if pos == target:
            return count

        for neighbor in get_neighbors(pos):
            if neighbor not in visited:
                todo.append((neighbor, count + 1))
                visited.add(neighbor)

    return -1


print(find_minimum_number_of_moves(0, 1 + 4j))
