def get_all_paths(graph, source, dest):
    paths = []

    def dfs(graph, source, dest, path):
        path.append(source)

        if source == dest:
            paths.append(path.copy())
        else:
            for neighbor in graph[source]:
                dfs(graph, neighbor, dest, path)

        path.pop()

    dfs(graph, source, dest, [])
    return paths


graph = {
    0: [1, 5],
    1: [2, 4],
    2: [3],
    3: [],
    4: [3],
    5: [1, 4]
}


print(get_all_paths(graph, 0, 3))
