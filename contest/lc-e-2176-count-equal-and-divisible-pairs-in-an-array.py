'''
Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.
'''
from typing import List
from collections import defaultdict


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        indices = defaultdict(list)

        for i, num in enumerate(nums):
            indices[num].append(i)

        pairs = 0
        for val in indices:
            num_vals = len(indices[val])
            if num_vals >= 2:
                for i in range(num_vals):
                    for j in range(i + 1, num_vals):
                        if indices[val][i] * indices[val][j] % k == 0:
                            pairs += 1

        return pairs


solution = Solution()
assert solution.countPairs([3, 1, 2, 2, 2, 1, 3], 2) == 4
assert solution.countPairs([1, 2, 3, 4], 1) == 0
