from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = min_sum = 0
        max_sum = nums[0]

        for num in nums:
            current_sum += num
            max_sum = max(max_sum, current_sum - min_sum)
            min_sum = min(min_sum, current_sum)

        return max_sum


solution = Solution()
assert solution.maxSubArray([-2, -1]) == -1
assert solution.maxSubArray([5, 4, -1, 7, 8]) == 23
assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert solution.maxSubArray([1]) == 1
