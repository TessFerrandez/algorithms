'''
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).
'''
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        positive = True
        for num in nums:
            if num == 0:
                return 0
            if num < 0:
                positive = not positive

        return 1 if positive else -1


solution = Solution()
assert solution.arraySign([-1, -2, -3, -4, 3, 2, 1]) == 1
assert solution.arraySign([1, 5, 0, 2, -3]) == 0
assert solution.arraySign([-1, 1, -1, 1, -1]) == -1
