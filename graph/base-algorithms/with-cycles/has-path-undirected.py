from collections import defaultdict, deque


def build_graph(edges):
    graph = defaultdict(lambda: [])

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    return graph


def has_path(graph, source, dest) -> bool:
    todo = deque([source])
    seen = set()

    while todo:
        current = todo.popleft()
        seen.add(current)

        if current == dest:
            return True

        for neighbor in graph[current]:
            if neighbor not in seen:
                todo.append(neighbor)

    return False


def has_path2(graph, source, dest, visited) -> bool:
    if source in visited:
        return False

    if source == dest:
        return True

    visited.add(source)

    for neighbor in graph[source]:
        if has_path2(graph, neighbor, dest, visited):
            return True

    return False


edges = [['i', 'j'], ['k', 'i'], ['m', 'k'], ['k', 'l'], ['o', 'n']]
graph = build_graph(edges)

print("Path i -> l:", has_path(graph, "i", "l"))
print("Path k -> o:", has_path(graph, "k", "o"))

print("Path i -> l:", has_path2(graph, "i", "l", set()))
print("Path k -> o:", has_path2(graph, "k", "o", set()))
