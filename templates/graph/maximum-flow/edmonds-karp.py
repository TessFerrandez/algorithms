# Edmonds-Karp Algorithm
from collections import defaultdict


def max_flow(n, capacity, source, sink):
    flow = defaultdict(int)

    # find path by using BFS
    def bfs():
        queue = [source]
        paths = {source:[]}
        if source == sink:
            return paths[source]
        while queue:
            u = queue.pop(0)
            for v in range(len(capacity)):
                if(capacity[(u, v)] - flow[(u, v)] > 0) and v not in paths:
                    paths[v] = paths[u] + [(u,v)]
                    if v == sink:
                        return paths[v]
                queue.append(v)
        return None

    path = bfs()

    while path:
        current_flow = min(capacity[(u, v)] - flow[(u, v)] for u,v in path)
        for u,v in path:
            flow[(u, v)] += current_flow
            flow[(v, u)] -= current_flow
        path = bfs()

    print([(edge, flow[edge]) for edge in flow if flow[edge] > 0])
    return sum(flow[(source, i)] for i in range(n))


c = {(0, 1): 3, (0, 2): 3, (1, 2): 2, (1, 3): 3, (2, 4): 2, (3, 4): 4, (3, 5): 2, (4, 5): 2, (5, 5): 3}
capacity = defaultdict(int)
for u, v in c:
    capacity[(u, v)] = c[(u, v)]
# assert max_flow(6, capacity, 0, 5) == 4

c = {(0, 1): 7, (0, 4): 4, (1, 2): 5, (1, 3): 3, (1, 4): 3, (2, 3): 3, (2, 5): 8, (3, 4): 2, (3, 5): 5}
capacity = defaultdict(int)
for u, v in c:
    capacity[(u, v)] = c[(u, v)]
print(max_flow(6, capacity, 0, 5))
