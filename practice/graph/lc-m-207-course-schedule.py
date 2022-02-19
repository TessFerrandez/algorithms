'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''
from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = defaultdict(set)
        post = defaultdict(list)

        for a, b in prerequisites:
            prereqs[a].add(b)
            post[b].append(a)

        can_take = []
        for course in range(numCourses):
            if course not in prereqs:
                can_take.append(course)

        taken = 0
        while can_take:
            course = can_take.pop()
            taken += 1

            for next_course in post[course]:
                prereqs[next_course].remove(course)
                if len(prereqs[next_course]) == 0:
                    can_take.append(next_course)

        return taken == numCourses


solution = Solution()
assert solution.canFinish(2, [[1, 0]])
assert not solution.canFinish(2, [[1, 0], [0, 1]])
