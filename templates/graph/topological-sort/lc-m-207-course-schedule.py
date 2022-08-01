from collections import defaultdict
from typing import List
from TopologicalSort import topological_sort


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for a, b in prerequisites:
            adj[b].append(a)

        return topological_sort(numCourses, adj) != []


solution = Solution()
assert solution.canFinish(2, [[1, 0]])
assert not solution.canFinish(2, [[1, 0], [0, 1]])
