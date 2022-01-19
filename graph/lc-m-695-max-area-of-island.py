from typing import List


def get_neighbors(graph, key):
    return [key + dir for dir in [-1j, 1, 1j, -1] if (key + dir) in graph]


def explore_size(graph, key, visited):
    if key in visited:
        return 0

    size = 1
    visited.add(key)

    for neighbor in get_neighbors(graph, key):
        size += explore_size(graph, neighbor, visited)

    return size


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        graph = {}

        for y, row in enumerate(grid):
            for x, num in enumerate(row):
                if num == 1:
                    graph[x + y * 1j] = 1

        max_size = 0
        visited = set()

        for key in graph:
            size = explore_size(graph, key, visited)
            max_size = max(max_size, size)

        return max_size


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
solution = Solution()
assert solution.maxAreaOfIsland(grid) == 6

grid = [[0,0,0,0,0,0,0,0]]
assert solution.maxAreaOfIsland(grid) == 0
