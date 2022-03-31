class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')

        parts = []
        current_num = ''

        for ch in s:
            if ch in ('+', '-', '*', '/'):
                parts.append(int(current_num))
                current_num = ''
                parts.append(ch)
            else:
                current_num += ch

        parts.append(int(current_num))

        n = len(parts)
        i = 0
        while i < n:
            if parts[i] in ('*', '/'):
                n1, n2 = parts[i - 1], parts[i + 1]
                res = n1 * n2 if parts[i] == '*' else n1 // n2
                parts = parts[:i - 1] + [res] + parts[i + 2:]
                n -= 2
            else:
                i += 1

        result = 0
        sign = '+'
        i = 0
        while i < n:
            if parts[i] in ('+', '-'):
                sign = parts[i]
            else:
                if sign == '+':
                    result += parts[i]
                else:
                    result -= parts[i]
            i += 1

        return result


solution = Solution()
assert solution.calculate(' 3+5 / 2') == 5
assert solution.calculate('3+2*2') == 7
assert solution.calculate(' 3/2 ') == 1
