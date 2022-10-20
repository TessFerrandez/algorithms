from functools import cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        @cache
        def can_make(target, index):
            if index >= n:
                return False
            if target < 0:
                return False
            if target == 0:
                return True
            return can_make(target - nums[index], index + 1) or can_make(target, index + 1)

        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        return can_make(target, 0)


solution = Solution()
assert solution.canPartition([1, 5, 11, 5])
assert not solution.canPartition([1, 2, 3, 5])
