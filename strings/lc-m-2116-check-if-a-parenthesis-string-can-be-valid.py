'''
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

If locked[i] is '1', you cannot change s[i].
But if locked[i] is '0', you can change s[i] to either '(' or ')'.
Return true if you can make s a valid parentheses string. Otherwise, return false.
'''
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        locked_open = []
        neutral = []

        for i in range(len(s)):

            if locked[i] == '0':
                neutral.append(i)
            elif locked[i] == '1':
                if s[i] == '(':
                    locked_open.append(i)
                else:
                    if locked_open:
                        locked_open.pop()
                    elif neutral:
                        neutral.pop()
                    else:
                        return False

        for i in reversed(locked_open):
            if neutral and neutral[-1] > i:
                neutral.pop()
            else:
                return False

        return len(neutral) % 2 == 0


solution = Solution()
assert solution.canBeValid('))()))', '010100')
assert solution.canBeValid('()()', '0000')
assert not solution.canBeValid(')', '0')
