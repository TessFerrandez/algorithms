# string
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strings = [''] * numRows
        index = 0
        while index < len(s):
            for i in range(numRows):
                if index >= len(s):
                    break
                strings[i] += s[index]
                index += 1
            for i in range(numRows - 2, 0, -1):
                if index >= len(s):
                    break
                strings[i] += s[index]
                index += 1
        return ''.join(strings)


solution = Solution()
assert solution.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert solution.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
assert solution.convert("A", 1) == "A"
