from typing import List
from UnionFind import UnionFind


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        uf = UnionFind(range(n))

        for node in range(len(graph)):
            if not graph[node]:
                continue
            first = graph[node][0]
            for neighbor in graph[node]:
                if uf.find(node) != uf.find(neighbor):
                    uf.union(first, neighbor)
                else:
                    return False
        return True


solution = Solution()
assert not solution.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]])
assert solution.isBipartite([[1,3],[0,2],[1,3],[0,2]])
