from math import inf
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lowest_so_far = 0
        prefix_sum = 0
        best = -inf

        for num in nums:
            prefix_sum = prefix_sum + num
            best = max(best, prefix_sum - lowest_so_far)
            lowest_so_far = min(lowest_so_far, prefix_sum)

        return best


solution = Solution()
assert solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert solution.maxSubArray([1]) == 1
assert solution.maxSubArray([5,4,-1,7,8]) == 23
