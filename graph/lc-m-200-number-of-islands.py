'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''
from typing import List


class Solution:
    def numIslands1(self, grid: List[List[str]]) -> int:
        def explore_land(graph, current, visited):
            if current in visited:
                return False

            visited.add(current)

            for diff in [-1j, 1, 1j, -1]:
                neighbor = current + diff
                if neighbor in graph:
                    explore_land(graph, neighbor, visited)

            return True

        def parse_grid(grid):
            graph = {}
            for y, row in enumerate(grid):
                for x, ch in enumerate(row):
                    if ch == '1':
                        graph[(x + y * 1j)] = True
            return graph

        graph = parse_grid(grid)

        count = 0
        visited = set()

        for land in graph:
            if explore_land(graph, land, visited):
                count += 1

        return count

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != '1':
                return

            grid[row][col] = '#'
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    dfs(row, col)
                    count += 1

        return count


solution = Solution()

grid = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]
assert solution.numIslands(grid) == 1

grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]
assert solution.numIslands(grid) == 3
