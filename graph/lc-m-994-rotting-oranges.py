'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
'''
from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        graph = {}
        todo = deque()
        visited = set()
        minutes = 0

        for y, row in enumerate(grid):
            for x, num in enumerate(row):
                if num == 1 or num == 2:
                    graph[(x + y * 1j)] = num
                    if num == 2:
                        todo.append(((x + y * 1j), 0))

        while todo:
            orange, minutes = todo.popleft()

            if orange in visited:
                continue

            visited.add(orange)

            for neighbor in [orange + dir for dir in [-1j, 1, 1j, -1] if orange + dir in graph and graph[orange + dir] == 1]:
                graph[neighbor] = 2
                todo.append((neighbor, minutes + 1))

        if 1 in graph.values():
            return -1

        return minutes


solution = Solution()

example1 = solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
print(example1)
assert example1 == 4

example2 = solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
print(example2)
assert example2 == -1

example3 = solution.orangesRotting([[0,2]])
print(example3)
assert example3 == 0
