class Solution:
    def makeGood(self, s: str) -> str:
        result = ''
        i = 0
        while i < len(s) - 1:
            if s[i].islower() and s[i + 1] == s[i].upper() or s[i].isupper() and s[i + 1] == s[i].lower():
                i += 2
            else:
                result += s[i]
                i += 1

        if i < len(s):
            result += s[-1]

        if result != s:
            return self.makeGood(result)
        else:
            return result


solution = Solution()
assert solution.makeGood('leEeetcode') == 'leetcode'
assert solution.makeGood('abBAcC') == ''
assert solution.makeGood('s') == 's'
assert solution.makeGood('Pp') == ''
