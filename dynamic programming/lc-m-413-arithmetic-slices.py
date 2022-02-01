'''
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

ALGO:
--------------
Check when the diff between this one an the previous changes
When it does - check how long the streak is - and based on the streak (using arithmetic sum) find out the number of sub strings
Ex. a string of 5 has 1(5) + 2(4) + 3(3) sub-arrays = n * (n + 1) // 2 [where n = 5 - 2] = 3 * 4 // 2 = 6 arrays

[1,     3,  5,  7,  9]
 INF    2   2   2   2
'''
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        MAX = 10 ** 9
        diff = MAX
        n = len(nums)
        last_seen = -1

        total_slices = 0

        for i in range(1, len(nums)):
            curr = nums[i] - nums[i - 1]
            if curr != diff:
                if diff != MAX:
                    if i - last_seen > 1:
                        streak = (i - last_seen) - 1
                        total_slices += streak * (streak + 1) // 2
                diff = curr
                last_seen = i

        if n - last_seen > 1 and diff != MAX:
            streak = (n - last_seen) - 1
            total_slices += streak * (streak + 1) // 2

        return total_slices


solution = Solution()
assert solution.numberOfArithmeticSlices([1, 2, 3, 4]) == 3
assert solution.numberOfArithmeticSlices([1]) == 0
