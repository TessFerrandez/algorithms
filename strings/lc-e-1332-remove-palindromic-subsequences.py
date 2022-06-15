class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == s[::-1]:
            return 1
        return 2


solution = Solution()
assert solution.removePalindromeSub('ababa')
assert solution.removePalindromeSub('abb')
assert solution.removePalindromeSub('baabb')
