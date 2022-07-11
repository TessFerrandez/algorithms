from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        has_odd = False
        total = 0

        for ch in counts:
            if counts[ch] % 2 != 0:
                has_odd = True
                counts[ch] -= 1
            total += counts[ch]
        return total + (1 if has_odd else 0)


solution = Solution()
assert solution.longestPalindrome('abccccdd') == 7
assert solution.longestPalindrome('a') == 1
