'''
Given an array of positive integers nums and a positive integer target,
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr]
of which the sum is greater than or equal to target.

If there is no such subarray, return 0 instead.

ALGO:
--------------
[2, 3, 1, 2, 4, 3]
1, 3, 1, 2 = 8          (4)
   3, 1, 2 = 6
   3, 1, 2, 4 = 10      (4)
      1, 2, 4 = 7       (3)
         2, 4 = 6
         2, 4, 3 = 9    (3)
            4, 3 = 7    (2)
'''
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = 10 ** 9
        left = 0

        num_sum = 0

        for right, num in enumerate(nums):
            num_sum += num
            while num_sum >= target:
                min_length = min(min_length, right - left + 1)
                num_sum -= nums[left]
                left += 1

        return min_length if min_length != 10 ** 9 else 0


solution = Solution()
assert solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
assert solution.minSubArrayLen(4, [1, 4, 4]) == 1
assert solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
