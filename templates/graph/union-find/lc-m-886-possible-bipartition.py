from collections import defaultdict
from typing import List
from UnionFind import UnionFind


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        uf = UnionFind(range(1, n + 1))
        graph = defaultdict(list)

        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        for node in range(1, n + 1):
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
assert solution.possibleBipartition(4, [[1, 2], [1, 3], [2, 4]])
assert not solution.possibleBipartition(3, [[1, 2], [1, 3], [2, 3]])
assert not solution.possibleBipartition(5, [[1,2],[2,3],[3,4],[4,5],[1,5]])
