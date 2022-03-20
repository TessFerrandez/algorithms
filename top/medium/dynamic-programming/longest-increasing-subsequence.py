from collections import defaultdict
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = defaultdict(int)

        for i in range(n - 1, -1, -1):
            max_len = 0
            for j in range(i, n):
                if nums[j] > nums[i]:
                    max_len = max(max_len, dp[j])
                dp[i] = 1 + max_len

        return max(dp.values())


solution = Solution()
assert solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
assert solution.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
assert solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
