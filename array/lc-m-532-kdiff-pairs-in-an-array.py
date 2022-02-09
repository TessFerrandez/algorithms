'''
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i < j < nums.length
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.
'''
from typing import List
from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        if k == 0:
            return sum(1 for num in counts if counts[num] > 1)
        else:
            return sum(1 for num in counts if num + k in counts)


solution = Solution()
assert solution.findPairs([3, 1, 4, 1, 5], 2) == 2
assert solution.findPairs([1, 2, 3, 4, 5], 1) == 4
assert solution.findPairs([1, 3, 1, 5, 4], 0) == 1
