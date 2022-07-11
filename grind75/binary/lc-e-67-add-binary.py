class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        if len(a) > len(b):
            a, b = b, a

        result = ''
        rest = 0
        for i in range(len(a)):
            curr = int(a[i]) + int(b[i]) + rest
            rest = 1 if curr >= 2 else 0
            result += str(curr % 2)

        for i in range(len(a), len(b)):
            curr = int(b[i]) + rest
            rest = 1 if curr == 2 else 0
            result += str(curr % 2)

        if rest == 1:
            result += '1'

        return result[::-1]


solution = Solution()
assert solution.addBinary('11', '1') == '100'
assert solution.addBinary('1010', '1011') == '10101'
