'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
'''
from typing import List
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        # explore pacific
        todo = deque([])
        for r in range(rows):
            todo.append((r, 0))
            pacific.add((r, 0))
        for c in range(cols):
            todo.append((0, c))
            pacific.add((0, c))

        while todo:
            r, c = todo.popleft()
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c] and (nr, nc) not in pacific:
                    pacific.add((nr, nc))
                    todo.append((nr, nc))

        # explore atlantic
        todo = deque([])
        for r in range(rows):
            todo.append((r, cols - 1))
            atlantic.add((r, cols - 1))
        for c in range(cols):
            todo.append((rows - 1, c))
            atlantic.add((rows - 1, c))

        while todo:
            r, c = todo.popleft()
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c] and (nr, nc) not in atlantic:
                    atlantic.add((nr, nc))
                    todo.append((nr, nc))

        return list(list(pos) for pos in pacific.intersection(atlantic))


solution = Solution()
assert solution.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]) == [[4, 0], [0, 4], [3, 1], [1, 4], [3, 0], [2, 2], [1, 3]]
assert solution.pacificAtlantic([[2,1],[1,2]]) == [[0, 1], [1, 0], [1, 1], [0, 0]]
