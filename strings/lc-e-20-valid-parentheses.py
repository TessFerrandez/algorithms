class Solution:
    def isValid(self, s: str) -> bool:
        closing = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in closing:
                if not stack:
                    return False
                else:
                    other = stack.pop()
                    if other != closing[ch]:
                        return False
            else:
                stack.append(ch)

        if stack:
            return False
        return True


solution = Solution()
assert solution.isValid('()') == True
assert solution.isValid('(){}[]') == True
assert solution.isValid('(]') == False
