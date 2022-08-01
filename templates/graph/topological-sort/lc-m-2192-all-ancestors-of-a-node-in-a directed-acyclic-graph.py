from typing import List
from TopologicalSort import get_ancestors


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        parents = [set() for _ in range(n)]

        for p, s in edges:
            parents[s].add(p)

        ancestors = get_ancestors(n, parents)
        return [sorted(list(parents)) for parents in ancestors]


solution = Solution()
assert solution.getAncestors(8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]) == [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
assert solution.getAncestors(5, [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]) == [[],[0],[0,1],[0,1,2],[0,1,2,3]]
