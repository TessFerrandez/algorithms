'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

ALGO:
----------------
Just xor all the numbers and you'll end up with the single one

[4, 1, 2, 1, 2]

100
001 XOR
---
101
010 XOR
---
111
001 XOR
---
110
010 XOR
---
100 = 4
'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result ^= num

        return result


solution = Solution()
assert solution.singleNumber([2, 2, 1]) == 1
assert solution.singleNumber([4, 1, 2, 1, 2]) == 4
assert solution.singleNumber([1]) == 1
