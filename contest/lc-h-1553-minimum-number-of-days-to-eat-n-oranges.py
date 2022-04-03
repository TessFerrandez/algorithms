'''h - 1553 minimum number of days ot eat n oranges'''
from functools import lru_cache


class Solution:
    # TLE input 9209408
    def minDays2(self, n: int) -> int:
        dp = {1: 1}

        for i in range(2, n + 1):
            best = 1 + dp[i - 1]
            if i % 2 == 0:
                best = min(best, 1 + dp[i // 2])
            if i % 3 == 0:
                best = min(best, 1 + dp[i - (2 * (i // 3))])
            dp[i] = best

        return dp[n]

    @lru_cache
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n
        return 1 + min(n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3))


solution = Solution()
assert solution.minDays(9209408) == 23
assert solution.minDays(56) == 6
assert solution.minDays(1) == 1
assert solution.minDays(10) == 4
assert solution.minDays(6) == 3
