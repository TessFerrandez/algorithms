from collections import deque
from typing import Set


def key_in_sets(key, sets):
    for set in sets:
        if key in set:
            return True

    return False


def get_reacheable(graph, key) -> Set[int]:
    visited = set()
    todo = deque([key])

    while todo:
        current = todo.popleft()

        if current in visited:
            continue

        visited.add(current)

        for neighbor in graph[current]:
            todo.append(neighbor)

    return visited


def largest_component(graph) -> int:
    sets = []

    for key in graph:
        if key_in_sets(key, sets):
            continue
        sets.append(get_reacheable(graph, key))

    max_size = 0
    for set in sets:
        max_size = max(max_size, len(set))

    return max_size


graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}

print(largest_component(graph))
