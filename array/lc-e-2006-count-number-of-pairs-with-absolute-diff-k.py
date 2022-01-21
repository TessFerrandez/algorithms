'''
Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.
'''
from typing import List
from collections import defaultdict


class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        num_map = defaultdict(int)

        for num in nums:
            num_map[num] += 1

        num_map = dict(num_map)

        total = 0
        for num in num_map:
            if num + k in num_map:
                total += num_map[num] * num_map[num + k]

        return total


solution = Solution()
assert solution.countKDifference([1, 2, 2, 1], 1) == 4
assert solution.countKDifference([1, 3], 3) == 0
assert solution.countKDifference([3, 2, 1, 5, 4], 2) == 3
