class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch for ch in s if ch.isalnum())
        s = s.lower()
        if len(s) <= 1:
            return True

        left, right = 0, len(s) - 1
        while right > left:
            if s[right] != s[left]:
                return False
            right -= 1
            left += 1

        return True


solution = Solution()
assert solution.isPalindrome(" ")
assert not solution.isPalindrome("0P")
assert solution.isPalindrome("A man, a plan, a canal: Panama")
assert not solution.isPalindrome("race a car")
