'''
Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Explanation:

taking the array [0, 0, 1, 1, 0, 0]
we have a sum  0 [1, 2, 1, 0, 1, 2]

any time you reach the same number eg. 0-0 1-1 or 2-2 in this case,
you have a balanced number of 0s and ones, so the best options in this case are

0 0 1 1 (0-0)
0 1 1 0 (1-1)
1 1 0 0 (2-2)

The longest length from A - A is the best option
'''
from typing import List


class Solution:
    def findMaxLength1(self, nums: List[int]) -> int:
        lengths = {0: -1}
        zeros, ones, max_len = 0, 0, 0

        for i, num in enumerate(nums):
            if num == 0:
                zeros += 1
            else:
                ones += 1

            if (zeros - ones) in lengths:
                max_len = max(max_len, i - lengths[(zeros - ones)])
            else:
                lengths[(zeros - ones)] = i

        return max_len

    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [-2] * (2 * n + 1)
        arr[n] = -1
        max_len, count = 0, 0

        for i, num in enumerate(nums):
            count += (-1 if num == 0 else 1)
            if arr[count + n] >= -1:
                max_len = max(max_len, i - arr[count + n])
            else:
                arr[count + n] = i

        return max_len


solution = Solution()
assert solution.findMaxLength([0, 1]) == 2
assert solution.findMaxLength([0, 1, 0]) == 2
