'''
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
'''
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0

        rest = num % 9
        return 9 if rest == 0 else rest


solution = Solution()
assert solution.addDigits(38) == 2
assert solution.addDigits(9) == 9
assert solution.addDigits(0) == 0

