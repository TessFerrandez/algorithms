'''
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.
'''
from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def get_neighbors(graph, position):
            x, y = position
            neighbors = [(x + dx, y + dy) for (dx, dy) in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]]
            return [neighbor for neighbor in neighbors if neighbor in graph]

        def parse_grid(grid):
            graph = {}
            target = (len(grid[0]) - 1, len(grid) - 1)

            for y, row in enumerate(grid):
                for x, n in enumerate(row):
                    if n == 0:
                        graph[(x, y)] = True

            return graph, target

        def bfs(graph, source, dest):
            todo = deque([(source, 1)])
            visited = set([source])

            if source == dest:
                return 1

            while todo:
                current, distance = todo.popleft()

                for neighbor in get_neighbors(graph, current):
                    if neighbor == dest:
                        return distance + 1

                    if neighbor not in visited:
                        visited.add(neighbor)
                        todo.append((neighbor, distance + 1))

            return -1

        graph, target = parse_grid(grid)
        start = (0, 0)
        if start not in graph or target not in graph:
            return -1

        return bfs(graph, start, target)


solution = Solution()
assert solution.shortestPathBinaryMatrix([[1, 0, 0],[1, 1, 0],[1, 1, 0]]) == -1
assert solution.shortestPathBinaryMatrix([[0, 1], [1, 0]]) == 2
assert solution.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]) == 4
