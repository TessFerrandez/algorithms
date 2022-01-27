'''
Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.

Intuition:
---------------
1. If we reach a 0, the sub-string ends since after that, the product can only be 0
2. If our number is positive,
    our positive streak is pos + 1
    our negative streak is neg + 1 if the negative streak was not 0 (if it was, then neg streak is 0)
3. If our number is negative
    our positive streak is neg + 1 if the negative streak was not 0 (if it was, then pos streak is 0)
    our negative streak is pos + 1
'''
from typing import List


class Solution:
    def getMaxLen1(self, nums: List[int]) -> int:
        n = len(nums)

        pos, neg = [0] * n, [0] * n

        if nums[0] > 0:
            pos[0] = 1
        if nums[0] < 0:
            neg[0] = 1

        ans = pos[0]

        for i in range(1, n):
            if nums[i] > 0:
                pos[i] = 1 + pos[i - 1]
                neg[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
            elif nums[i] < 0:
                pos[i] = 1 + neg[i - 1] if neg[i - 1] > 0 else 0
                neg[i] = 1 + pos[i - 1]
            ans = max(ans, pos[i])

        return ans

    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        pos, neg = 0, 0

        if nums[0] > 0:
            pos = 1
        if nums[0] < 0:
            neg = 1

        ans = pos
        for i in range(1, n):
            if nums[i] > 0:
                pos = 1 + pos
                neg = 1 + neg if neg > 0 else 0
            elif nums[i] < 0:
                pos, neg = 1 + neg if neg > 0 else 0, 1 + pos
            else:
                pos, neg = 0, 0
            ans = max(ans, pos)
        return ans


solution = Solution()
assert solution.getMaxLen([1, -2, -3, 4]) == 4
assert solution.getMaxLen([0, 1, -2, -3, -4]) == 3
assert solution.getMaxLen([-1, -2, -3, 0, 1])
