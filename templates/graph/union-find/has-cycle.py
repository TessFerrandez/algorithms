from UnionFind import UnionFind


# basic union find
def has_cycle2(edges):
    parents = {}

    def find_parent(node):
        if node not in parents:
            return node
        return find_parent(parents[node])

    def union(u, v):
        parents[u] = v

    for u, v in edges:
        parent_u, parent_v = find_parent(u), find_parent(v)
        if parent_u == parent_v:
            return True
        union(u, v)

    return False


assert has_cycle2([[0, 1], [1, 2], [0, 2]])
assert not has_cycle2([[0, 1], [1, 2], [0, 3]])


# optimized union find
def has_cycle1(edges, n_nodes):
    parent = [i for i in range(n_nodes)]
    size = [1 for _ in range(n_nodes)]

    def find(node):
        # compress the path
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]

        return node

    def union(u, v):
        if size[u] < size[v]:
            parent[u] = parent[v]
            size[v] += size[u]
        else:
            parent[v] = parent[u]
            size[u] += size[v]

    for u, v in edges:
        parent_u, parent_v = find(u), find(v)
        if parent_u == parent_v:
            return True
        union(u, v)

    return False


assert has_cycle1([[0, 1], [1, 2], [0, 2]], 3)
assert not has_cycle1([[0, 1], [1, 2], [0, 3]], 4)


# union find using class
def has_cycle(edges, n):
    uf = UnionFind(range(n))

    for u, v in edges:
        if uf.find(u) == uf.find(v):
            return True
        uf.union(u, v)
    return False


assert has_cycle([[0, 1], [1, 2], [0, 2]], 3)
assert not has_cycle([[0, 1], [1, 2], [0, 3]], 4)
