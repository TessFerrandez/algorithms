'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True

        if n < 10:
            return False

        digits = str(n)
        digit_sum = sum(int(digit) ** 2 for digit in digits)
        return self.isHappy(digit_sum)


solution = Solution()
assert solution.isHappy(19)
assert not solution.isHappy(2)
