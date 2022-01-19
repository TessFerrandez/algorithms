'''
Regular expression matching

a* matches _, a, aa, aaa, aaaa etc.
. matches any character
'''

class Solution:
    def isMatchDP(self, text: str, pattern: str) -> bool:
        '''
        dp bottom up
        '''
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        dp[-1][-1] = True

        for s_start in range(len(text), -1, -1):
            for p_start in range(len(pattern) - 1, -1, -1):
                first_match = s_start < len(text) and pattern[p_start] in {text[s_start], '.'}
                # if character 2 is a *
                if p_start + 1 < len(pattern) and pattern[p_start + 1] == '*':
                    # match if string[2:] is a match (i.e. we had 0 matches for this char)
                    # or if it matched the first character - and the rest of the string matches the current pattern
                    dp[s_start][p_start] = dp[s_start][p_start + 2] or first_match and dp[s_start + 1][p_start]
                else:
                    # if we didn't have a star - match if the pattern char == string star, and the rest of the
                    # string matches pattern[1:]
                    dp[s_start][p_start] = first_match and dp[s_start + 1][p_start + 1]

        return dp[0][0]

    def isMatch(self, text: str, pattern: str) -> bool:
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return self.isMatch(text, pattern[2:]) or first_match and self.isMatch(text[1:], pattern)
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


solution = Solution()
assert solution.isMatchDP('aa', 'a') == False
assert solution.isMatchDP('aa', 'a*') == True
assert solution.isMatchDP('aa', '.*') == True
assert solution.isMatchDP('mississippi', 'mis*is*p*.') == False
