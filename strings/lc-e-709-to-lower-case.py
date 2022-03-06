'''
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
'''
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


solution = Solution()
assert solution.toLowerCase('Hello') == 'hello'
assert solution.toLowerCase('here') == 'here'
assert solution.toLowerCase('LOVELY') == 'lovely'
