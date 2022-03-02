'''
Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
'''
from typing import List
from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        todo = deque([])

        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    todo.append((r, c, 0))
                    visited.add((r, c))

        max_steps = -1

        while todo:
            r, c, steps = todo.popleft()
            max_steps = max(max_steps, steps)
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    todo.append((nr, nc, steps + 1))

        return max_steps if max_steps != 0 else -1


solution = Solution()
assert solution.maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]) == 2
assert solution.maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) == 4
