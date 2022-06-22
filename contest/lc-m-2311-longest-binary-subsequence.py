class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        zeros = s.count('0')
        start = len(s) - 1

        while start >= 0 and int(s[start:], 2) <= k:
            start -= 1
        return zeros + s[start + 1:].count('1')


solution = Solution()
assert solution.longestSubsequence('1', 215358216) == 1
assert solution.longestSubsequence('1001010', 5) == 5
assert solution.longestSubsequence('00101001', 1) == 6
