'''
A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.
In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The first is not because its first two differences are positive, and the second is not because its last difference is zero.
A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

Given an integer array nums, return the length of the longest wiggle subsequence of nums.
'''
from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp_pos = [0] * n
        dp_neg = [0] * n

        for i in range(n - 1, -1, -1):
            max_pos, max_neg = 0, 0
            for j in range(i, n):
                if nums[j] > nums[i]:
                    max_pos = max(max_pos, dp_neg[j])
                elif nums[j] < nums[i]:
                    max_neg = max(max_neg, dp_pos[j])
            dp_pos[i] = max_pos + 1
            dp_neg[i] = max_neg + 1

        return max(max(dp_pos), max(dp_neg))


solution = Solution()
assert solution.wiggleMaxLength([1, 7, 4, 9, 2, 5]) == 6
assert solution.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]) == 7
assert solution.wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8]) == 2
