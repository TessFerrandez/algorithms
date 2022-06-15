from itertools import accumulate
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start = -1
        prefix_sum = list(accumulate(nums))
        max_sum = 0
        prev = {}

        for end in range(len(nums)):
            if nums[end] in prev and prev[nums[end]] > start:
                start = prev[nums[end]]
            if start == -1:
                max_sum = max(max_sum, prefix_sum[end])
            else:
                max_sum = max(max_sum, prefix_sum[end] - prefix_sum[start])
            prev[nums[end]] = end

        return max_sum


solution = Solution()
assert solution.maximumUniqueSubarray([4, 2, 4, 5, 6]) == 17
assert solution.maximumUniqueSubarray([5, 2, 1, 2, 5, 2, 1, 2, 5]) == 8
