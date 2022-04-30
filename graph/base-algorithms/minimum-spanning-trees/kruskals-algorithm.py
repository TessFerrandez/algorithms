'''
Given a graph with weighted edges. Find a way to connect all edges with the smallest
cost possible (ex. travelling salesman)

1. Sort all edges in non-decreasing order of their weight
2. Pick the smallest edge, check if it forms a cycle with the spanning tree formed so far (include it if it doesn't form a cycle)
3. Repeat step 2 until there are v-1 edges in the tree (using union find)
'''
class Graph:
    def __init__(self, nodes) -> None:
        self.nodes = nodes
        self.graph = []

    def add_edge(self, node_from, node_to, weight):
        self.graph.append([node_from, node_to, weight])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskals_mst(self):
        result = []
        node, edges = 0, 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent, rank = [], []

        for node in range(self.nodes):
            parent.append(node)
            rank.append(0)

        while edges < self.nodes - 1:
            fr, to, weight = self.graph[node]
            node += 1
            x = self.find(parent, fr)
            y = self.find(parent, to)
            if x != y:
                edges += 1
                result.append([fr, to, weight])
                self.union(parent, rank, x, y)

        minimum_cost = 0
        for fr, to, weight in result:
            minimum_cost += weight
        return minimum_cost


g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

print(g.kruskals_mst())
