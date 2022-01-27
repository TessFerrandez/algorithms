'''
You are given an integer array nums of length n.

Assume arrk to be an array obtained by rotating nums by k positions clock-wise. We define the rotation function F on nums as follow:

F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1].
Return the maximum value of F(0), F(1), ..., F(n-1).

The test cases are generated so that the answer fits in a 32-bit integer.
'''
from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        current_sum = sum(i * nums[i] for i in range(n))
        sum_nums = sum(nums)
        max_sum = current_sum

        for i in range(n - 1, 0, -1):
            current_sum += sum_nums - n * nums[i]
            max_sum = max(max_sum, current_sum)

        return max_sum


solution = Solution()
assert solution.maxRotateFunction([4, 3, 2, 6]) == 26
assert solution.maxRotateFunction([100]) == 0
