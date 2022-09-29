from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)

        length = 0
        for ch in counts:
            if counts[ch] > 1:
                length += (counts[ch] // 2) * 2

        for ch in counts:
            if counts[ch] % 2:
                length += 1
                break

        return length


solution = Solution()
assert solution.longestPalindrome("abccccdd") == 7
assert solution.longestPalindrome("a") == 1
