'''
Given an integer num, return three consecutive integers (as a sorted array) that sum to num. If num cannot be expressed as the sum of three consecutive integers, return an empty array.
'''
from typing import List


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num == 0:
            return [-1, 0, 1]

        if num % 3 == 0:
            div = num // 3
            return [div - 1, div, div + 1]
        else:
            return []


solution = Solution()
assert solution.sumOfThree(33) == [10, 11, 12]
assert solution.sumOfThree(4) == []
