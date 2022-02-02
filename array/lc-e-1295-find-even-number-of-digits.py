'''
Given an array nums of integers, return how many of them contain an even number of digits.
'''
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for num in nums if len(str(num)) % 2 == 0)


solution = Solution()
assert solution.findNumbers([12, 345, 2, 6, 7896]) == 2
assert solution.findNumbers([555, 901, 482, 1771]) == 1
