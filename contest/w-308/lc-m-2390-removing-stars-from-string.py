class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == '*':
                stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)


solution = Solution()
assert solution.removeStars("leet**cod*e") == "lecoe"
assert solution.removeStars("erase*****") == ""
