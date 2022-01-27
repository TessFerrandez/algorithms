'''
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

ALGO:
--------------
Naively, our maxProduct starting at any [i] would be nums[i] or nums[i] * maxProduct(nums[i + 1:])

Ex. [2, 3, -2, 4]
i = 0   2 or 2 * max([3, -2, 4])    => 6
i = 1   3 or 3 * max([-2, 4])       => 3
i = 2   -2 or -2 * max([4])         => -2
i = 3   4                           => 4

And our result would be the max of that

But what if we have [-2, 3, -4] = the solution is actually 24 but we would never see this... so we need to keep track of negative scores

i   nums[i]     min     max     min = min(nums[i], nums[i] * min, nums[i] * max)
2   -4          -4      -4      max = max(nums[i], nums[i] * min, nums[i] * max)
1   3           -12      3
0   -2          -6      24
'''
from typing import List


class Solution:
    # my solution
    def maxProduct1(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [-float('inf')] * n
        dp[n - 1] = nums[n - 1]

        dp_neg = [float('inf')] * n
        dp_neg[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            dp[i] = max([nums[i] * dp_neg[i + 1], nums[i], nums[i] * dp[i + 1]])
            dp_neg[i] = min([nums[i] * dp_neg[i + 1], nums[i], nums[i] * dp[i + 1]])

        return max(dp)

    # reduced to two memory positions
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        max_current = min_current = 1

        for num in nums:
            # need to save the values away as we will change them in the next step
            values = [num, num * max_current, num * min_current]
            max_current = max(values)
            min_current = min(values)
            max_product = max(max_product, max_current)

        return max_product


solution = Solution()
assert solution.maxProduct([0, -1, -2, -4]) == 8
assert solution.maxProduct([-2, 3, -4]) == 24
assert solution.maxProduct([2, 3, -2, 4]) == 6
assert solution.maxProduct([-2, 0, -1]) == 0
assert solution.maxProduct([0, -1, -2]) == 2
