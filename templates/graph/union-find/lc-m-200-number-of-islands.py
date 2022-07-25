from typing import List
from UnionFind import UnionFind


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        land = {(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == '1'}

        uf = UnionFind(land)
        for r, c in land:
            if (r - 1, c) in land:
                uf.union((r, c), (r - 1, c))
            if (r, c - 1) in land:
                uf.union((r, c), (r, c - 1))

        return uf.count


solution = Solution()
assert solution.numIslands([["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]]) == 1
assert solution.numIslands([["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]]) == 3
