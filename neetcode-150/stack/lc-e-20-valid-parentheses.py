class Solution:
    def isValid(self, s: str) -> bool:
        closing = {")": "(", "}": "{", "]": "["}
        stack = []

        for ch in s:
            if ch in closing:
                if not stack or stack[-1] != closing[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        if stack:
            return False

        return True


solution = Solution()
assert solution.isValid("()")
assert solution.isValid("()[]{}")
assert not solution.isValid("(]")
