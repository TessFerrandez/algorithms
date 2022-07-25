from typing import List
from UnionFind import UnionFind


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = set()
        for u, v in edges:
            nodes.add(u)
            nodes.add(v)

        uf = UnionFind(nodes)
        for u, v in edges:
            parent_u, parent_v = uf.find(u), uf.find(v)
            if parent_u == parent_v:
                return [u, v]
            uf.union(u, v)


solution = Solution()
assert solution.findRedundantConnection([[1,2],[1,3],[2,3]]) == [2, 3]
assert solution.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]) == [1, 4]
