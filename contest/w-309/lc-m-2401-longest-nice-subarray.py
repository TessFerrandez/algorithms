from collections import defaultdict
from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        longest, left, current_and = 0, 0, 0

        for right in range(len(nums)):
            while current_and & nums[right] > 0:
                current_and ^= nums[left]
                left += 1
            current_and |= nums[right]
            longest = max(longest, right - left + 1)

        return longest


solution = Solution()
assert solution.longestNiceSubarray([1,3,8,48,10]) == 3
assert solution.longestNiceSubarray([3,1,5,11,13]) == 1
