from typing import List
from UnionFind import UnionFind


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(range(n))

        for u in range(n):
            for v in range(n):
                if isConnected[u][v] == 1:
                    uf.union(u, v)

        return uf.count


solution = Solution()
assert solution.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]) == 2
assert solution.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]) == 3
