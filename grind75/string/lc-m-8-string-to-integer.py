class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1

        if i < n and s[i] in '+-':
            sign = 1 if s[i] == '+' else -1
            i += 1

        number = ''
        while i < n and s[i].isnumeric():
            number += s[i]
            i += 1

        number = (int(number) if number else 0) * sign
        if number < -2 ** 31:
            return -2 ** 31
        if number > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return number


solution = Solution()
assert solution.myAtoi('42') == 42
assert solution.myAtoi("   -42") == -42
assert solution.myAtoi("4193 with words") == 4193
