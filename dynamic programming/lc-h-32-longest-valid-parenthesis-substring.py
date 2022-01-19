'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
'''
class Solution:
    # from https://leetcode.com/problems/longest-valid-parentheses/discuss/14141/Pure-1D-DP-without-using-stack-(python)-with-detailed-explanation
    def longestValidParentheses(self, s: str) -> int:
        if s == "":
            return 0

        dp = [0 for _ in range(len(s))]

        for i in range(1, len(s)):
            if s[i] == ')':
                # string before + ()
                if s[i - 1] == '(':
                    # current = longest string before + 2 parens
                    dp[i] = dp[i - 2] + 2
                # string before + ( string between )
                # i - dp[i - 1] - 1 is the last ( not paired until this )
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    if dp[i - 1] > 0:
                        # string between was valid
                        # current = longest string before + string between + two parens
                        dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                    else:
                        # string between wasn't valid, so neither is this
                        dp[i] == 0

        return max(dp)


solution = Solution()

example5 = solution.longestValidParentheses("()(())")
assert example5 == 6

example4 = solution.longestValidParentheses("()(()")
assert example4 == 2

example1 = solution.longestValidParentheses("(()")
assert example1 == 2

example2 = solution.longestValidParentheses(")()())")
assert example2 == 4

example3 = solution.longestValidParentheses("")
assert example3 == 0
