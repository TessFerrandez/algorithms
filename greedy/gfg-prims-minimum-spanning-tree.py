import sys


class Graph():
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def print_MST(self, parent):
        print("Edge\tWeight")
        for i in range(1, self.V):
            print(f"{parent[i]}-{i}\t{self.graph[i][parent[i]]}")

    def min_key(self, key, mst_set):
        '''find the vertex with the minimu distance value'''
        min, min_index = sys.maxsize, -1

        for v in range(self.V):
            if key[v] < min and mst_set[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def prism_mst(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V

        key[0] = 0
        mst_set = [False] * self.V

        parent[0] = -1

        for cout in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and mst_set[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_MST(parent)


g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]
g.prism_mst()
