class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = {}
        longest = 0

        start = -1
        for i, ch in enumerate(s):
            if ch in lookup:
                start = max(start, lookup[ch])
            longest = max(longest, i - start)
            lookup[ch] = i

        return longest


solution = Solution()
assert solution.lengthOfLongestSubstring("abcabcbb") == 3
assert solution.lengthOfLongestSubstring("bbbbb") == 1
assert solution.lengthOfLongestSubstring("pwwkew") == 3
