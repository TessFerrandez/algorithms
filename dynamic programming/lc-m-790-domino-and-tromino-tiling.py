class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        dp = [0, 1, 2, 5]

        if n <= 3:
            return dp[n]
        for i in range(4, n + 1):
            dp.append(2 * dp[i - 1] + dp[i - 3])
            dp[-1] %= MOD

        return dp[n]


solution = Solution()
assert solution.numTilings(3) == 5
assert solution.numTilings(1) == 1
