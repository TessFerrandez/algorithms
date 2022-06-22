from typing import List


class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for row, col, price in prices:
            dp[row][col] = price

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                # Find all the possible first cut:
                for nc in range(1, col // 2 + 1):
                    dp[row][col] = max(dp[row][col], dp[row][nc] + dp[row][col - nc])
                for nr in range(1, row // 2 + 1):
                    dp[row][col] = max(dp[row][col], dp[nr][col] + dp[row - nr][col])

        return dp[m][n]


solution = Solution()
assert solution.sellingWood(3, 5, [[1,4,2],[2,2,7],[2,1,3]]) == 19
assert solution.sellingWood(4, 6, [[3,2,10],[1,4,2],[4,1,3]]) == 32
