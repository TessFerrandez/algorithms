from collections import deque


def shortest_path(graph, source, dest) -> int:
    todo = deque([(source, 0)])
    visited = set([source])

    if source == dest:
        return 0

    while todo:
        current, distance = todo.popleft()

        for neighbor in graph[current]:
            if neighbor == dest:
                return distance + 1

            if neighbor not in visited:
                visited.add(neighbor)
                todo.append((neighbor, distance + 1))

    return -1


graph = {
    'V': ['W', 'Z'],
    'W': ['V', 'X'],
    'X': ['W', 'Y'],
    'Y': ['X', 'Z'],
    'Z': ['V', 'Y']
}

print(shortest_path(graph, 'W', 'Z'))
