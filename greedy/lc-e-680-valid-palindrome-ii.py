'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        if s == s[::-1]:
            return True

        while left <= right:
            if s[left] != s[right]:
                # try removing the left non-matching
                s2 = s[:left] + s[left + 1:]
                if s2 == s2[::-1]:
                    return True

                # try removing the right non-matching
                s2 = s[:right] + s[right + 1:]
                if s2 == s2[::-1]:
                    return True

                # neither worked
                return False
            left += 1
            right -= 1

        return True


solution = Solution()
assert solution.validPalindrome('aba')
assert solution.validPalindrome('abca')
assert not solution.validPalindrome('abc')
