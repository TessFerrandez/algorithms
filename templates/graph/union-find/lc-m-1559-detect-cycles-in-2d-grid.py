from typing import List
from UnionFind import UnionFind


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])

        cells = [(r, c) for r in range(rows) for c in range(cols)]
        uf = UnionFind(cells)

        for r in range(rows):
            for c in range(cols):
                if r > 0 and grid[r][c] == grid[r - 1][c]:
                    if uf.find((r, c)) == uf.find((r - 1, c)):
                        return True
                    uf.union((r, c), (r - 1, c))
                if c > 0 and grid[r][c] == grid[r][c - 1]:
                    if uf.find((r, c)) == uf.find((r, c - 1)):
                        return True
                    uf.union((r, c), (r, c - 1))
        return False


solution = Solution()
assert solution.containsCycle([["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]])
assert solution.containsCycle([["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]])
assert not solution.containsCycle([["a","b","b"],["b","z","b"],["b","b","a"]])
