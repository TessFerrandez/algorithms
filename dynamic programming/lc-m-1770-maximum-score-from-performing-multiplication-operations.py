from functools import cache
from typing import List


class Solution:
    # MLE
    def maximumScore1(self, nums: List[int], multipliers: List[int]) -> int:
        n = len(multipliers)

        @cache
        def score(i, left, right):
            if i >= n:
                return 0
            return max(
                multipliers[i] * nums[left] + score(i + 1, left + 1, right),
                multipliers[i] * nums[right] + score(i + 1, left, right - 1))

        return score(0, 0, len(nums) - 1)

    # TLE
    def maximumScore2(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)

        @cache
        def dp(op, left):
            if op == m:
                return 0

            left_arr = nums[left] * multipliers[op] + dp(op + 1, left + 1)
            right_arr = nums[(n - 1) - (op - left)] * multipliers[op] + dp(op + 1, left)
            return max(left_arr, right_arr)

        # Zero operation done in the beginning
        return dp(0, 0)

    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)

        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for op in range(m - 1, -1, -1):
            for left in range(op, -1, -1):
                dp[op][left] = max(multipliers[op] * nums[left] + dp[op + 1][left + 1],
                                   multipliers[op] * nums[n - 1 - (op - left)] + dp[op + 1][left])

        return dp[0][0]


solution = Solution()
assert solution.maximumScore([1,2,3], [3,2,1]) == 14
assert solution.maximumScore([-5,-3,-3,-2,7,1], [-10,-5,3,4,6]) == 102
