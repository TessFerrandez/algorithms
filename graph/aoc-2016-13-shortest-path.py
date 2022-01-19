'''
Part 1: Find the shortest path between two nodes
Part 2: Find the max squares reached in 50 steps

Part 1
---------
Algorithm:      Breadth first search
State:          Square (x, y) - save distance
Target:         current = destination

Part 2
---------
Algorithm:      Breadth first search
State:          Square (x, y)
Target:         distance > 50
'''
from collections import deque


EMPTY = 0
WALL = 1
FAVORITE = 1364


def calculate_pos(position):
    x, y = position
    value = x * x + 3 * x + 2 * x * y + y + y * y + FAVORITE
    bin_str = bin(value)
    return EMPTY if bin_str.count('1') % 2 == 0 else WALL


def get_neighbors(graph, current):
    currx, curry = current
    valid_neighbors = []

    neighbors = [(currx, curry - 1), (currx + 1, curry), (currx, curry + 1), (currx - 1, curry)]
    for neighbor in neighbors:
        if neighbor[0] < 0 or neighbor[1] < 0:
            continue
        if neighbor not in graph:
            graph[neighbor] = calculate_pos(neighbor)
        if graph[neighbor] == EMPTY:
            valid_neighbors.append(neighbor)

    return valid_neighbors


def shortest_path(graph, source, dest) -> int:
    graph[source] = EMPTY
    graph[dest] = EMPTY

    todo = deque([(source, 0)])
    visited = set([source])

    if source == dest:
        return 0

    while todo:
        current, distance = todo.popleft()

        for neighbor in get_neighbors(graph, current):
            if neighbor == dest:
                return distance + 1

            if neighbor not in visited:
                visited.add(neighbor)
                todo.append((neighbor, distance + 1))

    return -1


def locations_reached(graph, source, steps) -> int:
    graph[source] = EMPTY

    todo = deque([(source, 0)])
    visited = set()

    while todo:
        current, distance = todo.popleft()

        if distance > steps:
            return len(visited)

        if current in visited:
            continue

        visited.add(current)

        for neighbor in get_neighbors(graph, current):
            todo.append((neighbor, distance + 1))

    return -1


graph = {}
print("Part 1:", shortest_path(graph, (1, 1), (31, 39)))
print("Part 2:", locations_reached(graph, (1, 1), 50))
