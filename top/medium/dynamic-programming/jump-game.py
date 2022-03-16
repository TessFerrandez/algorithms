from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n - 1] = True

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                if dp[j]:
                    dp[i] = True
                    break

        return dp[0]


solution = Solution()
assert solution.canJump([2, 3, 1, 1, 4])
assert not solution.canJump([3, 2, 1, 0, 4])
