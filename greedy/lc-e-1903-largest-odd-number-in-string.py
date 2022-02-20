'''
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.
'''
class Solution:
    def largestOddNumber(self, num: str) -> str:
        digits = list(num)

        while digits and int(digits[-1]) % 2 == 0:
            digits.pop()

        return ''.join(digits)


solution = Solution()
assert solution.largestOddNumber('52') == '5'
assert solution.largestOddNumber('4206') == ''
assert solution.largestOddNumber('35427') == '35427'
