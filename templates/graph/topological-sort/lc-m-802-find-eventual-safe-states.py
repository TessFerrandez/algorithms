from collections import defaultdict
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        WHITE, GRAY, BLACK = 0, 1, 2
        color = defaultdict(int)

        # returns true if node is not part of a cycle
        def dfs(node):
            if color[node] != WHITE:
                return color[node] == BLACK

            color[node] = GRAY
            for neighbor in graph[node]:
                if color[neighbor] == BLACK:
                    continue
                if color[neighbor] == GRAY or not dfs(neighbor):
                    return False
            color[node] = BLACK
            return True

        return list(filter(dfs, range(len(graph))))


solution = Solution()
assert solution.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]) == [2, 4, 5, 6]
assert solution.eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]]) == [4]
