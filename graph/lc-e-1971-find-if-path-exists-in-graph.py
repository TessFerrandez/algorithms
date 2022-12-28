from collections import defaultdict, deque
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)

        visited = set()
        todo = deque([source])

        while todo:
            node = todo.popleft()

            if node == destination:
                return True

            if node in visited:
                continue

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    todo.append(neighbor)

        return False


solution = Solution()
assert solution.validPath(3, [[0,1],[1,2],[2,0]], 0, 2)
assert not solution.validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5)
