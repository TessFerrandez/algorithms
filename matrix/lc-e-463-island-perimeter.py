from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        count = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue
                for nr, nc in (row - 1, col), (row + 1, col), (row, col + 1), (row, col - 1):
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        count += 1
                    elif grid[nr][nc] == 0:
                        count += 1

        return count


solution = Solution()
assert solution.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]) == 16
assert solution.islandPerimeter([[1]]) == 4
assert solution.islandPerimeter([[1, 0]]) == 4
