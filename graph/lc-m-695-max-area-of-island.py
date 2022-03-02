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
    def maxAreaOfIsland1(self, grid: List[List[int]]) -> int:
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

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] != 0:
                grid[row][col] = 0
                return 1 + dfs(row - 1, col) + dfs(row + 1, col) + dfs(row, col - 1) + dfs(row, col + 1)
            return 0

        areas = [dfs(r, c) for r in range(rows) for c in range(cols) if grid[r][c] != 0]
        return max(areas) if areas else 0


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
solution = Solution()
assert solution.maxAreaOfIsland(grid) == 6

grid = [[0,0,0,0,0,0,0,0]]
assert solution.maxAreaOfIsland(grid) == 0
