from typing import List
from UnionFind import UnionFind


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        cells = [(r, c) for r in range(rows) for c in range(cols)]

        uf = UnionFind(cells)
        for row in range(rows):
            for col in range(cols):
                if col > 0 and grid[row][col] in (1, 3, 5) and grid[row][col - 1] in (1, 4, 6):
                    uf.union((row, col), (row, col - 1))
                if row > 0 and grid[row][col] in (2, 5, 6) and grid[row - 1][col] in (2, 3, 4):
                    uf.union((row, col), (row - 1, col))

        return uf.find((0, 0)) == uf.find((rows - 1, cols - 1))


solution = Solution()
assert solution.hasValidPath([[2,4,3],[6,5,2]])
assert not solution.hasValidPath([[1,2,1],[1,2,1]])
assert not solution.hasValidPath([[1,1,2]])
