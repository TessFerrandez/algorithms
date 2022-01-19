class Solution:
    def lengthOfLongestSubstring_try1(self, s: str) -> int:
        longest_sub = 0
        s_len = len(s)

        for i in range(s_len):
            si = s[i]
            j = i + 1
            while j < s_len and s[j] not in si:
                si += s[j]
                j += 1
            longest_sub = max(longest_sub, j - i)

        return longest_sub

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        seen = {}
        start = 0

        for i, c in enumerate(s):
            if c in seen:
                start = max(start, seen[c] + 1)
            max_len = max(max_len, i - start + 1)
            seen[c] = i
        return max_len


solution = Solution()
assert solution.lengthOfLongestSubstring('abcabcbb') == 3
assert solution.lengthOfLongestSubstring('bbbbb') == 1
assert solution.lengthOfLongestSubstring('pwwkew') == 3
