from itertools import accumulate
from typing import List


class Solution:
    # kadane
    def maxSubArray1(self, nums: List[int]) -> int:
        max_num = max(nums)
        if max_num < 0:
            return max_num

        max_sum = max_num
        current_sum = 0

        for num in nums:
            # start over if it goes negative
            current_sum = max(current_sum + num, 0)
            max_sum = max(max_sum, current_sum)

        return max_sum

    # dp
    def maxSubArray2(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)

    # divide and conquer
    def maxSubArray(self, nums: List[int]) -> int:
        def helper(start, end):
            if start + 1 == end:
                return nums[start]
            mid = (start + end) // 2
            sum_left = helper(start, mid)
            sum_right = helper(mid, end)
            right = max(accumulate(nums[start: mid][::-1]))
            left = max(accumulate(nums[mid: end]))
            return max(sum_left, sum_right, left + right)

        return helper(0, len(nums))


solution = Solution()
assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert solution.maxSubArray([5, 4, -1, 7, 8]) == 23
assert solution.maxSubArray([1]) == 1
