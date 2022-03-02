'''
Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.
'''
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        reacheable = [0] * n

        for _, to_n in edges:
            reacheable[to_n] += 1

        return [i for i, reached_by in enumerate(reacheable) if reached_by == 0]


solution = Solution()
assert solution.findSmallestSetOfVertices(6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]) == [0, 3]
assert solution.findSmallestSetOfVertices(5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]) == [0, 2, 3]
