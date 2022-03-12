class Solution:
    def climbStairs2(self, n: int) -> int:
        if n < 0:
            return 0

        if n <= 1:
            return 1

        dp = [1, 1]
        for _ in range(2, n + 1):
            dp.append(dp[-1] + dp[-2])

        return dp[-1]

    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0

        if n <= 1:
            return 1

        prev, prev2 = 1, 1

        for _ in range(2, n + 1):
            current = prev + prev2
            prev, prev2 = prev2, current

        return prev2


solution = Solution()
assert solution.climbStairs(2) == 2
assert solution.climbStairs(3) == 3
