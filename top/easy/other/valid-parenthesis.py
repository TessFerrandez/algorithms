class Solution:
    def isValid(self, s: str) -> bool:
        closing = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in closing:
                if not stack:
                    return False
                if stack[-1] != closing[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack


solution = Solution()
assert solution.isValid('()')
assert solution.isValid('()[]{}')
assert not solution.isValid('(]')
assert not solution.isValid('(()')
