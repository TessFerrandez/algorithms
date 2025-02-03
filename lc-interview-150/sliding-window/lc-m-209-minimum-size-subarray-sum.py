# array, binary search, sliding window, prefix sum
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current_sum = 0
        left = 0
        right = 0
        min_length = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0


solution = Solution()
assert solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
assert solution.minSubArrayLen(4, [1, 4, 4]) == 1
assert solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
