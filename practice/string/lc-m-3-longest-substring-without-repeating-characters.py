from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        indices = defaultdict(lambda: -1)
        indices[s[0]] = 0

        last_len = 1
        max_len = 1

        for i in range(1, len(s)):
            last_len = min(last_len + 1, i - indices[s[i]])
            max_len = max(max_len, last_len)
            indices[s[i]] = i

        return max_len


solution = Solution()
assert solution.lengthOfLongestSubstring('abcabcbb') == 3
assert solution.lengthOfLongestSubstring('bbbbb') == 1
assert solution.lengthOfLongestSubstring('pwwkew') == 3
