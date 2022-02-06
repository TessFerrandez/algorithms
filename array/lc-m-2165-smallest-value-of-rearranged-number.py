'''
You are given an integer num. Rearrange the digits of num such that its value is minimized and it does not contain any leading zeros.

Return the rearranged number with minimal value.

Note that the sign of the number does not change after rearranging the digits.
'''
class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        number = 0
        if num < 0:
            # negative
            digits = sorted(list(str(num)[1:]), reverse=True)
            number = int('-' + ''.join(digits))
        else:
            # positive
            digits = sorted(list(str(num)))
            zeros = digits.count('0')
            number = digits[zeros]
            number += '0' * zeros
            number += ''.join(digits[zeros + 1:])
            number = int(number)

        return number


solution = Solution()
assert solution.smallestNumber(100) == 100
assert solution.smallestNumber(310) == 103
assert solution.smallestNumber(-7605) == -7650
