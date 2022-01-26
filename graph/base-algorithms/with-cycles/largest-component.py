def explore_size(graph, key, visited):
    if key in visited:
        return 0

    size = 1
    visited.add(key)

    for neighbor in graph[key]:
        size += explore_size(graph, neighbor, visited)

    return size


def largest_component(graph) -> int:
    max_size = 0
    visited = set()

    for key in graph:
        size = explore_size(graph, key, visited)
        max_size = max(max_size, size)

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
