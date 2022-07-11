class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = [ch.lower() for ch in s if ch.isalnum()]
        return clean == clean[::-1]


solution = Solution()
assert solution.isPalindrome("A man, a plan, a canal: Panama")
assert not solution.isPalindrome("race a car")
assert solution.isPalindrome(" ")
