from unittest import result


'''
You have n dice and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.
'''
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}

        def dp(n, target):
            if n == 0:
                return 0 if target > 0 else 1
            if (n, target) in memo:
                return memo[(n, target)]

            result = 0
            for f in range(max(0, target - k), target):
                result += dp(n - 1, f)

            memo[(n, target)] = result
            return result

        return dp(n, target) % (10 ** 9 + 7)


solution = Solution()
assert solution.numRollsToTarget(1, 6, 3) == 1
assert solution.numRollsToTarget(2, 6, 7) == 6
assert solution.numRollsToTarget(30, 30, 500) == 222616187
