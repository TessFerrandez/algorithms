'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
'''
from typing import List
from collections import defaultdict
from math import ceil


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = defaultdict(int)
        n = ceil(len(nums) / 2)

        for num in nums:
            hash[num] += 1
            if hash[num] >= n:
                return num

        return 0


solution = Solution()
assert solution.majorityElement([3, 2, 3]) == 3
assert solution.majorityElement([2, 2, 1, 1, 1, 2, 2,]) == 2
