from collections import defaultdict


class Graph:
    def __init__(self, edges=None):
        self.graph = defaultdict(list)
        if edges:
            for fr, to in edges:
                self.add_edge(fr, to)

    def add_edge(self, node, neighbor):
        self.graph[node].append(neighbor)

    def dfs(self, node, visited, components):
        visited.add(node)

        components[-1].add(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, visited, components)

    def fill_order(self, v, visited, stack):
        visited.add(v)

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.fill_order(neighbor, visited, stack)

        stack = stack.append(v)

    def get_reverse_graph(self):
        g = Graph()

        for node in self.graph:
            for neighbor in self.graph[node]:
                g.add_edge(neighbor, node)

        return g

    def get_strongly_connected_components(self):
        stack = []
        visited = set()

        nodes = list(self.graph.keys())

        for node in nodes:
            if node not in visited:
                self.fill_order(node, visited, stack)

        gr = self.get_reverse_graph()
        visited = set()
        components = [set()]

        while stack:
            node = stack.pop()
            if node not in visited:
                gr.dfs(node, visited, components)
                components.append(set())

        return components[:-1]


edges = [[1, 0], [0, 2], [2, 1], [0, 3], [3, 4]]
g = Graph(edges)
print(g.get_strongly_connected_components())

edges = [[0, 1], [1, 2], [2, 0], [1, 3]]
g = Graph(edges)
print(g.get_strongly_connected_components())
