from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def canPartition1(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        half = total_sum // 2
        n = len(nums)

        @cache
        def can_create(i, total):
            if total == 0:
                return True
            if total < 0 or i >= n:
                return False
            return can_create(i + 1, total) or can_create(i + 1, total - nums[i])

        return can_create(0, half)

    # bottom up
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        half = total_sum // 2
        can_create = defaultdict(bool)
        can_create[0] = True

        for num in nums:
            for remaining in range(half, -1, -1):
                can_create[remaining] = can_create[remaining] or can_create[remaining - num]

        return can_create[half]


solution = Solution()
assert solution.canPartition([1, 5, 11, 5])
assert not solution.canPartition([1, 2, 3, 5])
assert not solution.canPartition([1, 4, 5, 6])
