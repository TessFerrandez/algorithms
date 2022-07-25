from collections import defaultdict
from typing import List
from UnionFind import UnionFind


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        land = set()
        borders = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    land.add((row, col))
                    if row == 0 or row == rows - 1 or col == 0 or col == cols - 1:
                        borders.add((row, col))

        if not land:
            return 0

        uf = UnionFind(land)
        for r, c in land:
            if (r - 1, c) in land:
                uf.union((r, c), (r - 1, c))
            if (r, c - 1) in land:
                uf.union((r, c), (r, c - 1))

        border_groups = set()
        for node in borders:
            border_groups.add(uf.find(node))

        groups = defaultdict(int)
        for node in land:
            groups[uf.find(node)] += 1

        count = 0
        for group in groups:
            if group not in border_groups:
                count += groups[group]

        return count


solution = Solution()
assert solution.numEnclaves([[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]]) == 3
assert solution.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]) == 3
assert solution.numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]) == 0
