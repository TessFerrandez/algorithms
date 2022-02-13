'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        opening = {'}': '{', ']': '[', ')': '('}
        stack = []

        for ch in s:
            if ch not in opening:
                stack.append(ch)
            else:
                if not stack or stack[-1] != opening[ch]:
                    return False
                stack.pop()

        return stack == []


solution = Solution()
assert not solution.isValid('[')
assert solution.isValid('()')
assert solution.isValid('()[]{}')
assert not solution.isValid('(]')
