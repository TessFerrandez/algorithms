from collections import defaultdict
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)

        gn = {i: len(graph[i]) for i in range(n)}

        max_rank = 0
        for a in range(n - 1):
            for b in range(a + 1, n):
                rank = gn[a] + gn[b]
                if a in graph[b]:
                    rank -= 1
                max_rank = max(max_rank, rank)

        return max_rank


solution = Solution()
assert solution.maximalNetworkRank(4, [[0, 1], [0, 3], [1, 2], [1, 3]]) == 4
assert solution.maximalNetworkRank(5, [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]) == 5
assert solution.maximalNetworkRank(8, [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]) == 5
