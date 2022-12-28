class Solution:
    def calculate(self, s: str) -> int:
        # to fix case -(-2)+4
        s = s.replace('(-', '(0-')

        total = 0
        i, signs = 0, [1, 1]
        while i < len(s):
            # print('%11s   %-16s %2d' % (s[i:], signs, total))
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                total += signs.pop() * int(s[start:i])
                continue
            if c in '+-(':
                signs += signs[-1] * (1, -1)[c == '-'],
            elif c == ')':
                signs.pop()
            i += 1

        # print('%11s   %-16s %2d' % (s[i:], signs, total))

        return total


solution = Solution()
assert solution.calculate("1 + 1") == 2
assert solution.calculate("2-1 + 2") == 3
assert solution.calculate("(1+(4+5+2)-3)+(6+8)") == 23
assert solution.calculate("-(-2)+4") == 6
