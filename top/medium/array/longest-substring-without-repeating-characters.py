class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        start, max_len = 0, 0

        for i, ch in enumerate(s):
            if ch in char_map:
                start = max(start, char_map[ch] + 1)
            char_map[ch] = i
            max_len = max(max_len, i - start + 1)

        return max_len


solution = Solution()
assert solution.lengthOfLongestSubstring('abcabcbb') == 3
assert solution.lengthOfLongestSubstring('bbbbb') == 1
assert solution.lengthOfLongestSubstring('pwwkew') == 3
