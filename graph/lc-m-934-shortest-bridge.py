'''
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.
'''
from typing import List
from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def color_as_2(r, c):
            grid[r][c] = 2
            todo = deque([(r, c)])
            visited = set([(r, c)])

            while todo:
                r, c = todo.popleft()
                for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        todo.append((nr, nc))
                        visited.add((nr, nc))

            return visited

        def get_first_island():
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1:
                        return r, c
            return -1, -1

        # color first island as 2
        r, c = get_first_island()
        first_island = color_as_2(r, c)

        todo = deque([])
        visited = set()

        for r, c in first_island:
            todo.append((0, r, c))

        while todo:
            steps, r, c = todo.popleft()
            for nr, nc in [(r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)]:
                if 0 <= nc < cols and 0 <= nr < rows:
                    if grid[nr][nc] == 1:
                        return steps
                    if grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        todo.append((steps + 1, nr, nc))

        return -1


solution = Solution()
assert solution.shortestBridge([[0,0,0,1,1],
                                [0,0,0,1,0],
                                [0,0,0,1,1],
                                [0,0,1,0,1],
                                [0,0,1,1,0]]) == 1
assert solution.shortestBridge([[1,1,1,1,1],
                                [1,0,0,0,1],
                                [1,0,1,0,1],
                                [1,0,0,0,1],
                                [1,1,1,1,1]]) == 1
assert solution.shortestBridge([[0, 1], [1, 0]]) == 1
assert solution.shortestBridge([[0,1,0],[0,0,0],[0,0,1]]) == 2
