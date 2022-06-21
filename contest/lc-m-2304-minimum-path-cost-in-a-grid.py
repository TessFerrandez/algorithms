from typing import List


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        dp = grid[0][:]

        for row in range(1, rows):
            new_dp = []
            for col in range(cols):
                best = 10 ** 9
                for idx, i in enumerate(grid[row - 1]):
                    best = min(best, dp[idx] + grid[row][col] + moveCost[i][col])
                new_dp.append(best)
            dp = new_dp

        return min(dp)


solution = Solution()
assert solution.minPathCost([[5,3],[4,0],[2,1]], [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]]) == 17
assert solution.minPathCost([[5,1,2],[4,0,3]], [[12,10,15],[20,23,8],[21,7,1],[8,1,13],[9,10,25],[5,3,2]]) == 6
