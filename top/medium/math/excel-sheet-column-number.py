class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        i = 0

        for ch in reversed(columnTitle):
            result += (26 ** i) * (ord(ch) - ord('A') + 1)
            i += 1

        return result


solution = Solution()
assert solution.titleToNumber('A') == 1
assert solution.titleToNumber('AB') == 28
assert solution.titleToNumber('ZY') == 701
