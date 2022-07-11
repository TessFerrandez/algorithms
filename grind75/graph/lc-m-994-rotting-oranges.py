from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque([])
        fresh = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh.add((row, col))
                elif grid[row][col] == 2:
                    rotten.append((row, col, 0))

        while rotten and fresh:
            row, col, minutes = rotten.popleft()
            for nr, nc in (row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1):
                if (nr, nc) in fresh:
                    fresh.remove((nr, nc))
                    rotten.append((nr, nc, minutes + 1))

        if fresh:
            return -1
        if rotten:
            return rotten[-1][2]
        return 0


solution = Solution()
assert solution.orangesRotting([[2,1,1],[1,1,1],[0,1,2]]) == 2
assert solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
assert solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
assert solution.orangesRotting([[0, 2]]) == 0
