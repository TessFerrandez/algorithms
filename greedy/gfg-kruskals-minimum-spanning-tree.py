'''
https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/?ref=lbp

Given an connected - undirected graph
A spanning tree is a sub-graph that connects
all vertices.

A minimum spanning tree, is the spanning tree
with the least total weight

    1 - 2 - 3
  / |   |\  | \
 0  |   8 \ |  4
  \ | / |  \| /
    7 - 6 - 5

Weigths (after sorting)

Weight   Src    Dest
1         7      6
2         8      2
2         6      5
4         0      1
4         2      5
6         8      6
7         2      3
7         7      8
8         0      7
8         1      2
9         3      4
10        5      4
11        1      7
14        3      5

Minimum spanning tree (MST):

    1   2 - 3
  /     |\    \
 0      8 \    4
  \        \
    7 - 6 - 5

1. Sort all edges in increasing order of their weight
2. Pick the smallest edge.
    if it forms a cycle - discard it
    if not - include it
3. Repeat #2 until we have V-1 edges (V = # vertices/nodes)
'''
class Graph:
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append([u, v, weight])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        else:
            return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        # attach smaller rank tree under root
        # of higher rank tree (Union by rank)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def Kruskal_MST(self):
        result = []
        i, e = 0, 0

        # 1. sort edges by weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        # create V subsets with single elements
        parent = [node for node in range(self.V)]
        rank = [0 for _ in range(self.V)]

        while e < self.V - 1:
            # 2. Pick smallest edge
            u, v, weight = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # if adding it does not cause a cycle
            # include it
            if x != y:
                e += 1
                result.append([u, v, weight])
                self.union(parent, rank, x, y)

        minimum_cost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimum_cost += weight
            print(f"({u}-{v}-{weight})")

        print("Minimum cost:", minimum_cost)


g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(1, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.Kruskal_MST()
