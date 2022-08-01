from collections import defaultdict


# topological sort using colors - checks for cycles
def topological_sort(n, adj):
    WHITE, GRAY, BLACK = 0, 1, 2
    global found_cycle

    def dfs(node):
        global found_cycle

        if found_cycle:
            return
        if color[node] == GRAY:
            found_cycle = True
        if color[node] == WHITE:
            color[node] = GRAY
            for neighbor in adj[node]:
                dfs(neighbor)
            color[node] = BLACK
            order.append(node)

    color = defaultdict(int)
    order = []
    found_cycle = False

    for node in range(n):
        if found_cycle:
            break
        if color[node] == WHITE:
            dfs(node)

    return [] if found_cycle else order[::-1]


# basic topological sort
def topological_sort2(n, edges):
    visited = set()
    order = []

    def dfs(node):
        visited.add(node)
        for neighbor in edges[node]:
            if neighbor in visited:
                continue
            dfs(neighbor)
        order.append(node)

    for node in range(n):
        if node in visited:
            continue
        dfs(node)

    return order[::-1]


def get_ancestors(n, parents):
    ancestors = [-1 for _ in range(n)]

    def dfs(node):
        if ancestors[node] == -1:
            anc = set()
            for parent in parents[node]:
                parent_ancestors = dfs(parent)
                anc.add(parent)
                anc = anc | parent_ancestors
            ancestors[node] = anc
        return ancestors[node]

    for node in range(n):
        dfs(node)

    return ancestors


def test_topological_sort():
    edges = {0: [1, 2, 3], 1: [3, 4], 2: [], 3: [2], 4: []}
    assert topological_sort(5, edges) == [0, 1, 4, 3, 2]

    edges = {0: [1, 2, 3], 1: [3, 4], 2: [], 3: [2], 4: []}
    assert topological_sort2(5, edges) == [0, 1, 4, 3, 2]

    edges = {0: [1], 1: []}
    assert topological_sort(2, edges)

    edges = {0: [1], 1: [0]}
    assert not topological_sort(2, edges)


# test_topological_sort()
