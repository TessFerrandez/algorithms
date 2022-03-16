from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(row, col):
            if grid[row][col] != '1' or (row, col) in visited:
                return False

            todo = deque([(row, col)])

            while todo:
                r, c = todo.popleft()

                if (r, c) in visited:
                    continue

                visited.add((r, c))

                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                        todo.append((nr, nc))

            return True

        count = 0
        for r in range(rows):
            for c in range(cols):
                if bfs(r, c):
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
