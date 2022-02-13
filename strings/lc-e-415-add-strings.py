'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i1, i2 = len(num1) - 1, len(num2) - 1

        result = 0
        rest = 0
        potens = 0
        ord0 = ord('0')

        while i1 >= 0 or i2 >= 0:
            col_sum = rest

            if i1 >= 0:
                col_sum += ord(num1[i1]) - ord0
            if i2 >= 0:
                col_sum += ord(num2[i2]) - ord0

            if col_sum >= 10:
                rest = col_sum // 10
                col_sum = col_sum % 10
            else:
                rest = 0

            result += col_sum * 10 ** potens
            potens += 1
            i1 -= 1
            i2 -= 1

        if rest > 0:
            result += rest * 10 ** potens

        return str(result)


solution = Solution()
assert solution.addStrings('1', '9') == '10'
assert solution.addStrings('11', '123') == '134'
assert solution.addStrings('456', '77') == '533'
assert solution.addStrings('0', '0') == '0'
