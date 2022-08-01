from collections import defaultdict
from typing import List


class Solution:
    def loudAndRich1(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        for u, v in richer:
            graph[v].append(u)

        answer = [None] * n

        def dfs(node):
            # want the least quiet person in the subtree
            if not answer[node]:
                answer[node] = node
                for child in graph[node]:
                    candidate = dfs(child)
                    if quiet[candidate] < quiet[answer[node]]:
                        answer[node] = candidate
            return answer[node]

        return list(map(dfs, range(n)))

    def loudAndRich2(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        answer = n * [-1]

        # directed graph
        pre, suc = [set() for _ in range(n)], [set() for _ in range(n)]
        indegree = n * [0]

        for p1, p2 in richer:
            suc[p1].add(p2)
            pre[p2].add(p1)
            indegree[p2] += 1

        # visit richest people first
        current_level = {person for person in range(n) if indegree[person] == 0}
        for person in current_level:
            answer[person] = person

        while current_level:
            next_level = set()
            for p1 in current_level:
                for p2 in suc[p1]:
                    indegree[p2] -= 1

                    if indegree[p2] == 0:
                        answer[p2] = p2
                        for p3 in pre[p2]:
                            if quiet[answer[p3]] < quiet[answer[p2]]:
                                answer[p2] = answer[p3]
                        next_level.add(p2)
            current_level = next_level

        return answer

    # topological sort
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)

        def dfs(node):
            # avoids recursion
            if answer[node] == -1:
                answer[node] = node

                for child in graph[node]:
                    # loudest in child (richer) sub-tree
                    current = dfs(child)

                    # set me to that loundness if children are louder
                    if quiet[current] < quiet[answer[node]]:
                        answer[node] = current

            return answer[node]

        graph = defaultdict(set)
        for x, y in richer:
            graph[y].add(x)

        answer = [-1] * n
        for i in range(n):
            dfs(i)
        return answer


solution = Solution()
assert solution.loudAndRich([[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], [3,2,5,4,6,1,7,0]) == [5,5,2,5,4,5,6,7]
assert solution.loudAndRich([], [0]) == [0]
