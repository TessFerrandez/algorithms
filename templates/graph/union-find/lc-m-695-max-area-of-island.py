from collections import defaultdict
from typing import List
from UnionFind import UnionFind


class Solution:
    def maxAreaOfIsland1(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        parent = defaultdict()
        size = defaultdict()

        in_bound = lambda r, c: 0 <= r < rows and 0 <= c < cols
        answer = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    parent[(row, col)] = (row, col)
                    size[(row, col)] = 1

        def find(u):
            if u == parent[u]:
                return u
            parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            u = find(u)
            v = find(v)

            if u != v:
                if size[u] >= size[v]:
                    parent[v] = u
                    size[u] += size[v]
                    return size[u]
                else:
                    parent[u] = v
                    size[v] += size[u]
                    return size[v]
            return 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    if answer == 0:
                        answer = 1
                    for nr, nc in (row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1):
                        if in_bound(nr, nc) and grid[nr][nc] == 1:
                            answer = max(answer, union((row, col), (nr, nc)))

        return answer

    # using union find class
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ones = {(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == 1}
        if not ones:
            return 0

        uf = UnionFind(ones)

        for r, c in ones:
            if (r - 1, c) in ones:
                uf.union((r, c), (r - 1, c))
            if (r, c - 1) in ones:
                uf.union((r, c), (r, c - 1))

        return uf.largest_component_size()


solution = Solution()
assert solution.maxAreaOfIsland([[1, 0, 1, 0, 0], [0, 0, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 1], [0, 1, 1, 1, 1]]) == 9
assert solution.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]) == 6
assert solution.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]) == 0
