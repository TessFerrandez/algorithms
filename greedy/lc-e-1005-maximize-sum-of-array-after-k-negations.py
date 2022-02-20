'''
Given an integer array nums and an integer k, modify the array in the following way:

choose an index i and replace nums[i] with -nums[i].
You should apply this process exactly k times. You may choose the same index i multiple times.

Return the largest possible sum of the array after modifying it in this way.
'''
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        total = sum(nums)

        for _ in range(k):
            min_val = min(nums)
            total -= 2 * min_val
            nums.remove(min_val)
            nums.append(-min_val)

        return total


solution = Solution()
assert solution.largestSumAfterKNegations([4, 2, 3], 1) == 5
assert solution.largestSumAfterKNegations([3, -1, 0, 2], 3) == 6
assert solution.largestSumAfterKNegations([2, -3, -1, 5, -4], 2) == 13
