'''
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...
'''
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
