class Solution:
    def distinctSequences(self, n: int) -> int:
        if n == 1:
            return 6

        dp = [[0, 1, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 0, 1], [1, 0, 0, 0, 1, 0]]
        dp1 = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

        for i in range(3, n + 1):
            for d in range(6):
                for p in range(6):
                    dp1[d][p] = 0
                    if dp[d][p] != 0:
                        for pp in range(6):
                            if d != pp:
                                dp1[d][p] = (dp1[d][p] + dp[p][pp]) % 1000000007
            dp, dp1 = dp1, dp

        return sum(sum(dp[i]) for i in range(6)) % 1000000007


solution = Solution()
assert solution.distinctSequences(4) == 184
assert solution.distinctSequences(2) == 22
