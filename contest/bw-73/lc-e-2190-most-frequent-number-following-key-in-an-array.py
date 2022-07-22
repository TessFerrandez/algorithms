'''
You are given a 0-indexed integer array nums. You are also given an integer key, which is present in nums.

For every unique integer target in nums, count the number of times target immediately follows an occurrence of key in nums. In other words, count the number of indices i such that:

0 <= i <= n - 2,
nums[i] == key and,
nums[i + 1] == target.
Return the target with the maximum count. The test cases will be generated such that the target with maximum count is unique.
'''
from typing import List
from collections import defaultdict


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        counts = defaultdict(int)

        for i in range(len(nums) - 1):
            if nums[i] == key:
                counts[nums[i + 1]] += 1

        max_count = max(counts.values())
        for count in counts:
            if counts[count] == max_count:
                return count

        return 0


solution = Solution()
assert solution.mostFrequent([1,100,200,1,100], 1) == 100
assert solution.mostFrequent([2,2,2,2,3], 2) == 2
