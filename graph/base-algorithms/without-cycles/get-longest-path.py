def get_all_path_lengths(graph, source, dest):
    path_lenghts = []

    def dfs(graph, source, dest, path_len):
        if source == dest:
            path_lenghts.append(path_len + 1)
        else:
            for neighbor in graph[source]:
                dfs(graph, neighbor, dest, path_len + 1)

    dfs(graph, source, dest, 0)
    return path_lenghts


def get_longest_path_length(graph, source, dest):
    return max(get_all_path_lengths(graph, source, dest))


graph = {
    0: [1, 5],
    1: [2, 4],
    2: [3],
    3: [],
    4: [3],
    5: [1, 4]
}

print(get_all_path_lengths(graph, 0, 3))
print(get_longest_path_length(graph, 0, 3))
