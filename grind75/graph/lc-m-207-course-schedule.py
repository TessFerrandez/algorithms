from collections import defaultdict
from typing import List


class Solution:
    # topological sort
    # a --> b => a, b
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        white, gray, black = set(range(numCourses)), set(), set()
        prereqs = defaultdict(list)

        for pre, post in prerequisites:
            prereqs[post].append(pre)

        def dfs(class_number):
            gray.add(class_number)
            for prereq in prereqs[class_number]:
                if prereq in black:
                    continue
                if prereq in gray:
                    return True
                if dfs(prereq):
                    return True

            gray.remove(class_number)
            black.add(class_number)
            return False

        while white:
            class_number = white.pop()
            if dfs(class_number):
                return False
        return True


solution = Solution()
assert solution.canFinish(2, [[1, 0]])
assert not solution.canFinish(2, [[1, 0], [0, 1]])
assert solution.canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
