class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        '''
        # dp[x] = the answer when Alice has x points
        dp[x] = 1.0 when k <= x <= n else 0.0
        for x from k - 1 to 0:
            dp[x] = (dp[x + 1] + ... + dp[x + maxPts]) / maxPts
        return dp[0]
        '''
        dp = [0.0] * (n + maxPts + 1)

        for x in range(k, n + 1):
            dp[x] = 1.0

        s = min(n - k + 1, maxPts)
        for x in range(k - 1, -1, -1):
            dp[x] = s / float(maxPts)
            s += dp[x] - dp[x + maxPts]

        return dp[0]


solution = Solution()
assert solution.new21Game(10, 1, 10) == 1.0
assert solution.new21Game(6, 1, 10) == 0.6
assert abs(solution.new21Game(21, 17, 10) - 0.7328) <= 0.001
