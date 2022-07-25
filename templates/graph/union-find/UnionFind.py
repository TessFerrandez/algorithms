class UnionFind:
    def __init__(self, nodes) -> None:
        self.size = {}
        self.parent = {}
        self.count = 0
        for node in nodes:
            self.size[node] = 1
            self.parent[node] = node
            self.count += 1

    def find(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if u != v:
            self.parent[u] = v
            self.size[v] += self.size[u]
            self.count -= 1

    def largest_component_size(self):
        max_size = 0
        for node in self.parent:
            if self.parent[node] == node and self.size[node] > max_size:
                max_size = self.size[node]

        return max_size

    def num_regions(self):
        return self.count
