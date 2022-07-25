from typing import List
from UnionFind import UnionFind


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        rows, cols = len(grid), len(grid[0])
        cells = set()
        for row in range(rows):
            for col in range(cols):
                cells.add((row, col, 'U'))
                cells.add((row, col, 'D'))
                cells.add((row, col, 'L'))
                cells.add((row, col, 'R'))

        uf = UnionFind(cells)

        for row in range(rows):
            for col in range(cols):
                if row > 0:
                    uf.union((row, col, 'U'), (row - 1, col, 'D'))
                if col > 0:
                    uf.union((row, col, 'L'), (row, col - 1, 'R'))
                if grid[row][col] == " ":
                    uf.union((row, col, 'U'), (row, col, 'L'))
                    uf.union((row, col, 'L'), (row, col, 'D'))
                    uf.union((row, col, 'D'), (row, col, 'R'))
                elif grid[row][col] == "/":
                    uf.union((row, col, 'U'), (row, col, 'L'))
                    uf.union((row, col, 'D'), (row, col, 'R'))
                else:
                    uf.union((row, col, 'U'), (row, col, 'R'))
                    uf.union((row, col, 'D'), (row, col, 'L'))

        return uf.count


solution = Solution()
assert solution.regionsBySlashes([" /","/ "]) == 2
assert solution.regionsBySlashes([" /","  "]) == 1
assert solution.regionsBySlashes(["/\\","\\/"]) == 5
