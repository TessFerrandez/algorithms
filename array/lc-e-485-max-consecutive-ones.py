'''
'''
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        current_ones = 0

        for num in nums:
            if num == 1:
                current_ones += 1
            else:
                max_ones = max(current_ones, max_ones)
                current_ones = 0

        max_ones = max(current_ones, max_ones)
        return max_ones


solution = Solution()
assert solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3
assert solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2
