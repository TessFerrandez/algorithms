class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        if num < 0:
            digits = list(str(num)[1:])
            digits.sort(reverse=True)
            return -1 * int(''.join(digits))

        else:
            digits = list(str(num))
            digits.sort()
            zeros = digits.count('0')
            if zeros > 0:
                digits[0], digits[zeros] = digits[zeros], digits[0]
            return int(''.join(digits))


solution = Solution()
assert solution.smallestNumber(310) == 103
assert solution.smallestNumber(3100) == 1003
assert solution.smallestNumber(-7605) == -7650
