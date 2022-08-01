'''
Pick a random node as starter

1. Pick the edge with the lowest cost from any node
already in the graph to a node that is not yet added
2. Rinse and repeat until all the nodes are in the graph
'''
from heapq import heappop, heappush
from math import inf
from itertools import count


# PRIMs basic function with matrix for cost
class Graph:
    def __init__(self, n) -> None:
        self.N = n
        self.graph = [[0 for column in range(n)] for row in range(n)]

    def add_edge(self, u, v, cost):
        self.graph[u][v] = cost
        self.graph[v][u] = cost

    def generate_mst(self, parent):
        mst = []
        for i in range(1, self.N):
            mst.append((parent[i], i, self.graph[i][parent[i]]))
        return mst

    def min_key(self, key, mst_set):
        min = inf
        for node in range(self.N):
            if key[node] < min and not mst_set[node]:
                min = key[node]
                min_index = node

        return min_index

    def prim_mst(self):
        # key value used to pick minimum weight edge in cut
        key = [inf] * self.N
        parent = [None] * self.N
        mst_set = [False] * self.N

        # pick first node
        key[0] = 0
        parent[0] = -1

        for _ in range(self.N):
            # pick the minimum distance node
            # from the set of nodes we haven't processed yet
            u = self.min_key(key, mst_set)

            # put the minimum distance node in the
            # shortest path tree
            mst_set[u] = True

            # update dist values of adjacent nodes
            # of the picked node only if the current
            # distance is greater than the new distance
            # and the vertex is not in the shortest path tree
            for v in range(self.N):
                if self.graph[u][v] > 0 and not mst_set[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        return self.generate_mst(parent)


# Optimized PRIM with heap for cost
# No need to have nodes from 0 - n
def prim_minimum_spanning_tree_cost(graph):
    tiebreak = count().__next__     # factory for tie-breaking
    total_cost = 0
    explored = set()
    start = next(iter(graph))
    unexplored = [(0, tiebreak(), start, -1)]
    edges = []

    while unexplored:
        cost, _, winner, from_node = heappop(unexplored)
        if winner not in explored:
            explored.add(winner)
            total_cost += cost
            edges.append((from_node, winner, cost))
            for neighbor, cost in graph[winner]:
                if neighbor not in explored:
                    heappush(unexplored, (cost, tiebreak(), neighbor, winner))

    return edges[1:], total_cost


def generate_graph(adj):
    g = Graph(len(adj))
    for u in adj:
        for v, cost in adj[u]:
            g.add_edge(u, v, cost)
    return g


def test_prim():
    adj_list = {
        0: [[1, 2], [3, 6]],
        1: [[0, 2], [2, 3], [3, 8], [4, 5]],
        2: [[1, 3], [4, 7]],
        3: [[0, 6], [1, 8], [4, 9]],
        4: [[1, 5], [2, 7], [3, 9]]
    }
    graph = generate_graph(adj_list)
    assert graph.prim_mst() == [(0, 1, 2), (1, 2, 3), (0, 3, 6), (1, 4, 5)]

    edges, total = prim_minimum_spanning_tree_cost(adj_list)
    assert edges == [(0, 1, 2), (1, 2, 3), (1, 4, 5), (0, 3, 6)]
    assert total == 16

    adj_list = {
        0: [[1, 2], [3, 1], [4, 4]],
        1: [[0, 2], [2, 3], [3, 3], [5, 7]],
        2: [[1, 3], [3, 5], [5, 8]],
        3: [[0, 1], [1, 3], [2, 5], [4, 9]],
        4: [[0, 4], [3, 9]],
        5: [[1, 7], [2, 8]]
    }
    graph = generate_graph(adj_list)
    assert graph.prim_mst() == [(0, 1, 2), (1, 2, 3), (0, 3, 1), (0, 4, 4), (1, 5, 7)]

    edges, total = prim_minimum_spanning_tree_cost(adj_list)
    assert edges == [(0, 3, 1), (0, 1, 2), (1, 2, 3), (0, 4, 4), (1, 5, 7)]
    assert total == 17

    adj_list = {'a': [['b', 5]], 'b': [['a', 5]]}
    edges, total = prim_minimum_spanning_tree_cost(adj_list)
    assert edges == [('a', 'b', 5)]
    assert total == 5


# test_prim()
