class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""

        for i, ch in enumerate(palindrome):
            if ch != 'a':
                new_palindrome = palindrome[:i] + 'a' + palindrome[i + 1:]
                if new_palindrome != new_palindrome[::-1]:
                    return new_palindrome

        return palindrome[:-1] + 'b'


solution = Solution()
assert solution.breakPalindrome("b") == ""
assert solution.breakPalindrome("aba") == "abb"
assert solution.breakPalindrome("abccba") == "aaccba"
assert solution.breakPalindrome("a") == ""
