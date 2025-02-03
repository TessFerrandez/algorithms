# two pointers, string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if left < right and s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


solution = Solution()
assert solution.isPalindrome("A man, a plan, a canal: Panama")
assert not solution.isPalindrome("race a car")
assert solution.isPalindrome("a")
assert solution.isPalindrome(" ")
