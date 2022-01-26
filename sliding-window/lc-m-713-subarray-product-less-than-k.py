'''
Given an array of integers nums and an integer k,
return the number of contiguous subarrays where the product of all the elements
in the subarray is strictly less than k.

ALGORITHM
-----------------
Ex. [10, 5, 2, 6]

left    right   product     sub-arrays              total (right - left + 1)
0       0       10          [10]                    +1  1
0       1       50          [5], [10, 5]            +2  3
0       2       100         -
1       2       10          [2], [5, 2]             +2  5
1       3       60          [6], [2, 6], [5, 2, 6]  +3  8
'''
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        total, left = 0, 0
        product = 1

        for right, num in enumerate(nums):
            product *= num
            while product >= k:
                product /= nums[left]
                left += 1
            total += right - left + 1

        return total


solution = Solution()
assert solution.numSubarrayProductLessThanK([10, 5, 2, 6], 100) == 8
assert solution.numSubarrayProductLessThanK([1, 2, 3], 0) == 0
