'''
https://www.geeksforgeeks.org/union-find/

Ex.

0
| \
|  1
| /
2

For each edge, make subsets using both the vertices
of the edge - if both are in the same subset, a cycle is found

Initially set them to -1 (only one item in every subset):
 0  1  2
-1 -1 -1

E 0-1 - they are in different subsets (-1, -1)
        take the union, either making 0, parent of 1 or 1 parent of 0

 0  1  2    # 1 is parent of 0
 1 -1 -1

E 1-2 - 1 is in subset 1 and 2 is in subset 2, taken union

 0  1  2    # 2 is parent of 1 (2 is now {0, 1, 2})
 1  2 -1

E 0-2 - 0 is in subset 2 and 2 is in subset 2 => cycle
        How are 0 same as 2??? 0->1->2
'''
from collections import defaultdict


class Graph:
    def __init__(self, vertices) -> None:
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        else:
            return self.find_parent(parent, parent[i])

    def union(self, parent, x, y):
        parent[x] = y

    def is_cyclic(self):
        parent = [-1] * self.V

        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)


g = Graph(3)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
assert g.is_cyclic() == True
