'''
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
'''
from importlib.abc import SourceLoader


class Solution:
    def numberOfSteps2(self, num: int) -> int:
        steps = 0

        while num > 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1
            steps += 1

        return steps

    def numberOfSteps(self, num: int) -> int:
        bstr = bin(num)
        # '0' means divide
        # '1' means - 1 and then divide
        bstr_sum =  bstr.count('0') + 2 * bstr.count('1')
        # 0b0010 - first 0 shouldn't be counted and total reduced by 1 (for the last 0)
        return bstr_sum - 2

solution = Solution()
assert solution.numberOfSteps(14) == 6
assert solution.numberOfSteps(8) == 4
assert solution.numberOfSteps(123) == 12
