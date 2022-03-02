'''
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
'''
from math import ceil


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low == 0:
            return ceil(high / 2)
        else:
            return ceil(high / 2) - ceil((low - 1) / 2)


solution = Solution()
assert solution.countOdds(0, 7) == 4
assert solution.countOdds(3, 7) == 3
assert solution.countOdds(8, 10) == 1
