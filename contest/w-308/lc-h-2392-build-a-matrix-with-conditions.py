from collections import deque
from typing import List


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(graph):
            nxt, in_degree = [set() for _ in range(k)], [0] * k
            todo, order = deque(), []
            graph = set([tuple(node) for node in graph])

            for i, j in graph:
                nxt[i - 1].add(j - 1)
                in_degree[j - 1] += 1

            for i in range(k):
                if in_degree[i] == 0:
                    todo.append(i)

            while todo:
                current = todo.popleft()
                order.append(current)
                for candidate in nxt[current]:
                    in_degree[candidate] -= 1
                    if in_degree[candidate] == 0:
                        todo.append(candidate)

            return order if len(order) == k else []

        rows, cols = topo_sort(rowConditions), topo_sort(colConditions)
        if not rows or not cols:
            return []

        grid = [[0] * k for _ in range(k)]
        for i in range(k):
            grid[rows.index(i)][cols.index(i)] = i + 1
        return grid


solution = Solution()
assert solution.buildMatrix(3, [[1,2],[3,2]], [[2,1],[3,2]]) == [[0, 0, 1], [3, 0, 0], [0, 2, 0]]
assert solution.buildMatrix(3, [[1,2],[2,3],[3,1],[2,3]], [[2,1]]) == []
