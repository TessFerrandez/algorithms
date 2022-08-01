'''
based on disjoint union set - good for if you have disjoint sets

To start with all the nodes are "singles"
all edges are sorted by cost (in non-decreasing order)

1. Pick the lowest edge - if it combines two subtrees, add it
2. Rinse and repeat for all edges (this allows disjoint sets)
'''


# edges are [[u, v, cost], ...]
def kruskals1(nodes, edges):
    result = []
    parent = {node: node for node in nodes}

    edges.sort(key=lambda x: x[2])

    total_cost = 0
    for u, v, cost in edges:
        if parent[u] != parent[v]:
            total_cost += cost
            result.append([u, v, cost])

            old_parent, new_parent = parent[u], parent[v]
            for node in nodes:
                if parent[node] == old_parent:
                    parent[node] = new_parent

    return result, parent


# optimized kruskals
def kruskals(nodes, edges):
    parent = {node: node for node in nodes}
    rank = {node: 0 for node in nodes}

    def find(v):
        if v == parent[v]:
            return v
        parent[v] = find(parent[v])
        return parent[v]

    def union(u, v):
        u, v = find(u), find(v)
        if u != v:
            if rank[u] < rank[v]:
                u, v = v, u
            parent[v] = u
            if rank[u] == rank[v]:
                rank[u] += 1

    edges.sort(key=lambda x: x[2])
    results = []

    for u, v, weight in edges:
        if find(u) != find(v):
            results.append([u, v, weight])
            union(u, v)

    return results, parent


def test_kruskals():
    edges = [[1, 2, 10], [4, 3, 12], [4, 1, 41], [2, 3, 23]]
    roads, _ = kruskals(range(1, 5), edges)
    assert roads == [[1, 2, 10], [4, 3, 12], [2, 3, 23]]

    edges = [[1, 2, 20], [4, 5, 40], [3, 2, 30]]
    roads, _ = kruskals(range(1, 6), edges)
    assert roads == [[1, 2, 20], [3, 2, 30], [4, 5, 40]]


test_kruskals()
