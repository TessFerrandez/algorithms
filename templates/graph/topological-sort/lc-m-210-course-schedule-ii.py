from collections import defaultdict
from typing import List
from TopologicalSort import topological_sort


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(list)
        for a, b in prerequisites:
            prereqs[b].append(a)

        return topological_sort(numCourses, prereqs)


solution = Solution()
assert solution.findOrder(2, [[1, 0]]) == [0, 1]
assert solution.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) == [0, 2, 1, 3]
assert solution.findOrder(1, []) == [0]
