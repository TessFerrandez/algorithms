class Solution:
    def maximum69Number(self, num: int) -> int:
        digits = list(str(num))
        for i, digit in enumerate(digits):
            if digit == '6':
                digits[i] = '9'
                return int(''.join(digits))
        return num


solution = Solution()
assert solution.maximum69Number(9669) == 9969
assert solution.maximum69Number(9996) == 9999
