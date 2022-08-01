from collections import defaultdict
from math import inf
from Prims import prim_minimum_spanning_tree_cost


def roads_in_hackerland(n_cities, roads):
    graph = defaultdict(list)

    for city1, city2, dist in roads:
        graph[city1].append((city2, dist))
        graph[city2].append((city1, dist))

    mst, _ = prim_minimum_spanning_tree_cost(graph)

    mst_graph = defaultdict(list)
    for city1, city2, dist in mst:
        mst_graph[city1].append((city2, dist))
        mst_graph[city2].append((city1, dist))

    total_path = 0

    def dfs(i, j, past):
        if i == j:
            return 0
        shortest = inf

        for next, dist in mst_graph[i]:
            if next != past:
                path = dfs(next, j, i)
                if path != -1:
                    shortest = min(shortest, dist + path)

        if shortest == inf:
            return -1
        else:
            return shortest

    for i in range(1, n_cities + 1):
        for j in range(i + 1, n_cities + 1):
            total_path += dfs(i, j, -1)

    return total_path


roads = [[1, 3, 32], [4, 5, 1], [2, 1, 8], [3, 2, 2], [4, 3, 16], [4, 2, 4]]
assert roads_in_hackerland(5, roads) == 68
