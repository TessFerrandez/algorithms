class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x >= 0:
            digits = list(str(x))
        else:
            sign = -1
            digits = list(str(x)[1:])

        digits.reverse()
        value = sign * int(''.join(digits))
        if -(2 ** 31) <= value <= (2 ** 31) - 1:
            return value
        else:
            return 0


solution = Solution()
assert solution.reverse(123) == 321
assert solution.reverse(-123) == -321
assert solution.reverse(120) == 21
