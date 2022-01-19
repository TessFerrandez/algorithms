from collections import deque
from typing import Dict, Tuple, Union


def get_neighbors(grid, current, key_ring):
    possible = [current + dir for dir in [-1j, 1, 1j, -1]]

    neighbors = []
    for neighbor in possible:
        if grid[neighbor] == ".":
            neighbors.append((neighbor, key_ring))
        elif grid[neighbor] in "abcdefghijklmnopqrstuvwxyz" and grid[neighbor] not in key_ring:
            new_key_ring = key_ring + grid[neighbor]
            new_key_ring = ''.join(sorted(new_key_ring))
            neighbors.append((neighbor, new_key_ring))
        elif grid[neighbor] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            if grid[neighbor].lower() in key_ring:
                neighbors.append((neighbor, key_ring))

    return neighbors


def get_shortest_path(start, grid, all_keys):
    todo = deque([(start, "")])
    previous: Dict[Tuple[complex, str], Union[Tuple[complex, str], None]] = {(start, ""): None}

    target = None

    while todo:
        current, key_ring = todo.popleft()
        if key_ring == all_keys:
            target = (current, key_ring)
            break

        for neighbor in get_neighbors(grid, current, key_ring):
            if neighbor not in previous:
                previous[neighbor] = (current, key_ring)
                todo.append(neighbor)

    # target was never found
    if not target:
        return []

    # build path
    path = []
    current = target

    while current:
        path.append(current)
        current = previous[current]

    path.reverse()
    return path


def parse_grid(raw_input):
    grid = {}

    for y, line in enumerate(raw_input.strip().splitlines()):
        for x, ch in enumerate(line):
            if ch == "@":
                ch = "."
            grid[x + y*1j] = ch

    return grid


raw_input1 = '''#########
#b.A.@.a#
#########'''

grid = parse_grid(raw_input1)
shortest_path = get_shortest_path(5 + 1j, grid, "ab")
# print(shortest_path)
print(len(shortest_path) - 1)
