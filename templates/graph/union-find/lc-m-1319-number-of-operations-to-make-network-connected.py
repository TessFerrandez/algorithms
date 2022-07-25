from typing import List
from UnionFind import UnionFind


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        n_cables = len(connections)
        if n_cables < n - 1:
            return -1

        uf = UnionFind(range(n))

        for u, v in connections:
            uf.union(u, v)

        return uf.count - 1


solution = Solution()
assert solution.makeConnected(4, [[0,1],[0,2],[1,2]]) == 1
assert solution.makeConnected(6, [[0,1],[0,2],[0,3],[1,2],[1,3]]) == 2
assert solution.makeConnected(6, [[0,1],[0,2],[0,3],[1,2]]) == -1
