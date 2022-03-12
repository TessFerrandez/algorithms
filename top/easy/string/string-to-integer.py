class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if s == '':
            return 0

        sign = 1
        i = 0

        if s[0] == '-':
            sign = -1
            i = 1
        elif s[0] == '+':
            i = 1

        number = ''
        while i < len(s) and s[i].isnumeric():
            number += s[i]
            i += 1

        result = int(number) * sign
        if result < -2 ** 31:
            return -2 ** 31
        elif result > (2 ** 31 - 1):
            return (2 ** 31 - 1)
        else:
            return result


solution = Solution()
assert solution.myAtoi('42') == 42
assert solution.myAtoi("   -42") == -42
assert solution.myAtoi("4193 with words") == 4193
