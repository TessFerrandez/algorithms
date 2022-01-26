def explore(graph, current, visited):
    if current in visited:
        return False

    visited.add(current)

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)

    # finished exploring all its neighbors
    return True


def connected_components_count(graph) -> int:
    count = 0
    visited = set()

    for key in graph:
        if explore(graph, key, visited):
            count += 1

    return count


graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}

print(connected_components_count(graph))
