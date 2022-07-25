from typing import List
from UnionFind import UnionFind


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        borders = set()
        land = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    land.add((row, col))
                    if row == 0 or col == 0 or row == rows - 1 or col == cols - 1:
                        borders.add((row, col))

        uf = UnionFind(land)
        for r, c in land:
            if (r - 1, c) in land:
                uf.union((r, c), (r - 1, c))
            if (r, c - 1) in land:
                uf.union((r, c), (r, c - 1))

        groups = set()
        for cell in land:
            groups.add(uf.find(cell))

        border_groups = set()
        for cell in borders:
            border_groups.add(uf.find(cell))

        count = 0
        for group in groups:
            if group not in border_groups:
                count += 1

        return count


solution = Solution()
assert solution.closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]) == 2
assert solution.closedIsland([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]) == 1
assert solution.closedIsland([[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]) == 2
