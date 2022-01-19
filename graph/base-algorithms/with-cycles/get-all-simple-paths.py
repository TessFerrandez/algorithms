def get_all_simple_paths(graph, source, dest):
    paths = []

    def dfs(graph, source, dest, visited, path):
        visited.add(source)
        path.append(source)

        if source == dest:
            paths.append(path.copy())
        else:
            for neighbor in graph[source]:
                if neighbor not in visited:
                    dfs(graph, neighbor, dest, visited, path)

        path.pop()
        visited.remove(source)

    dfs(graph, source, dest, set(), [])
    return paths


def count_all_simple_paths(graph, source, dest):
    path_count = [0]

    def dfs(graph, source, dest, visited):
        visited.add(source)

        if source == dest:
            path_count[0] += 1
        else:
            for neighbor in graph[source]:
                if neighbor not in visited:
                    dfs(graph, neighbor, dest, visited)

        visited.remove(source)

    dfs(graph, source, dest, set())
    return path_count[0]


graph = {
    0: [1, 2, 3],
    1: [3],
    2: [0, 1, 3],
    3: []
}

print(get_all_simple_paths(graph, 0, 3))
print(count_all_simple_paths(graph, 0, 3))
