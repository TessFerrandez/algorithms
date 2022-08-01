from collections import defaultdict
from typing import List
from TopologicalSort import get_ancestors


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parents = defaultdict(list)
        for a, b in prerequisites:
            parents[b].append(a)

        ancestors = get_ancestors(numCourses, parents)
        answers = []
        for u, v in queries:
            answers.append(u in ancestors[v])

        return answers


solution = Solution()
assert solution.checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]]) == [False, True]
assert solution.checkIfPrerequisite(2, [], [[0, 1], [1, 0]]) == [False, False]
assert solution.checkIfPrerequisite(3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]]) == [True, True]
