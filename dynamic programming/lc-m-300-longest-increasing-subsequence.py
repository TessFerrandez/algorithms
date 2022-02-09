'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
'''
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            max_len = 0
            for j in range(i, n):
                if nums[j] > nums[i]:
                    max_len = max(max_len, dp[j])
            dp[i] = 1 + max_len

        return max(dp)


solution = Solution()
assert solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
assert solution.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
assert solution.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
