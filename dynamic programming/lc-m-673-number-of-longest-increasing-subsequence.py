'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

dp saves
-----------------
1. Maximum length of increasing sub sequence from i
2. Number of sub sequences with this length

Eg. dp[0] = [4, 2] means we have 2 subsequences from i=0 that are 4 elements long
'''
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0]] * n

        for i in range(n - 1, -1, -1):
            max_length = 0
            num_max_lengths = 1
            lengths = []

            for j in range(i, n):
                if nums[j] > nums[i]:
                    lengths.append(dp[j])
            if lengths:
                max_length = max(length[0] for length in lengths)
                num_max_lengths = sum(length[1] for length in lengths if length[0] == max_length)

            dp[i] = [1 + max_length, num_max_lengths]

        max_length = max(element[0] for element in dp)
        return sum(element[1] for element in dp if element[0] == max_length)


solution = Solution()
assert solution.findNumberOfLIS([1, 3, 5, 4, 7]) == 2
assert solution.findNumberOfLIS([2, 2, 2, 2, 2]) == 5
