from typing import List
from UnionFind import UnionFind


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        computers = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    computers.append((r, c))

        uf = UnionFind(computers)
        for i in range(len(computers)):
            for j in range(i + 1, len(computers)):
                if computers[i][0] == computers[j][0] or computers[i][1] == computers[j][1]:
                    uf.union(computers[i], computers[j])

        count = 0
        for computer in computers:
            if uf.parent[computer] == computer and uf.size[computer] > 1:
                count += uf.size[computer]

        return count


solution = Solution()
assert solution.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]) == 4
assert solution.countServers([[1,0],[0,1]]) == 0
assert solution.countServers([[1,0],[1,1]]) == 3
