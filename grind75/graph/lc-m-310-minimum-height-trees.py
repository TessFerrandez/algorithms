from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        adj = defaultdict(set)

        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        leaves = set()
        for node in adj:
            if len(adj[node]) == 1:
                leaves.add(node)

        while n > 2:
            n -= len(leaves)
            next_leaves = set()
            for leave in leaves:
                for neighbor in adj[leave]:
                    adj[neighbor].remove(leave)
                    if len(adj[neighbor]) <= 1:
                        next_leaves.add(neighbor)
            leaves = next_leaves

        return list(leaves)


solution = Solution()
assert solution.findMinHeightTrees(6, [[0, 1], [0, 2], [0, 3], [3, 4], [4, 5]]) == [3]
assert solution.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]) == [1]
assert solution.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]) == [3, 4]
assert solution.findMinHeightTrees(1, []) == [0]
