   from collections import deque


def has_path_dfs(graph, source, dest) -> bool:
    stack = [source]

    while stack:
        current = stack.pop()

        if current == dest:
            return True

        for neighbor in graph[current]:
            stack.append(neighbor)

    return False


def has_path_bfs(graph, source, dest) -> bool:
    queue = deque([source])

    while queue:
        current = queue.popleft()

        if current == dest:
            return True

        for neighbor in graph[current]:
            queue.append(neighbor)

    return False


graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}


print(has_path_bfs(graph, 'f', 'k'))
print(has_path_bfs(graph, 'j', 'f'))
print(has_path_dfs(graph, 'f', 'k'))
print(has_path_dfs(graph, 'j', 'f'))