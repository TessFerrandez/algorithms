'''
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
'''
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openers, closers = [], []

        for i, ch in enumerate(list(s)):
            if ch == '(':
                openers.append(i)
            if ch == ')':
                if openers:
                    openers.pop()
                else:
                    closers.append(i)

        to_remove = openers + closers
        to_remove.sort(reverse=True)

        result = ''
        for i, ch in enumerate(s):
            if to_remove and to_remove[-1] == i:
                to_remove.pop()
            else:
                result += ch
        return result


solution = Solution()
assert solution.minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de"
assert solution.minRemoveToMakeValid("a)b(c)d") == "ab(c)d"
assert solution.minRemoveToMakeValid("))((") == ""
