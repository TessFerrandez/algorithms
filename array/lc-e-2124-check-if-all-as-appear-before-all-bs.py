'''
Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.
'''
class Solution:
    def checkString(self, s: str) -> bool:
        a, b = 0, 0
        try:
            b = s.index('b')
        except ValueError:
            return True

        try:
            a = s[::-1].index('a')
        except ValueError:
            return True

        a = len(s) - a - 1
        return a < b


solution = Solution()
assert solution.checkString('aaabbb')
assert not solution.checkString('abab')
assert solution.checkString('bbb')
