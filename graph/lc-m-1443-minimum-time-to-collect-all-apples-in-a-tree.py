from collections import defaultdict
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)

        def dfs(node, parent):
            if node not in graph:
                return 0

            total_time = 0
            child_time = 0

            for child in graph[node]:
                if child == parent:
                    continue
                child_time = dfs(child, node)
                if child_time > 0 or hasApple[child]:
                    total_time += child_time + 2

            return total_time

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        return dfs(0, -1)


solution = Solution()
assert solution.minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False, False, True, False, True, True, False]) == 8
assert solution.minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,False,True,False]) == 6
assert solution.minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,False,False,False,False,False]) == 0
