class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = {}

        longest, current = 0, 0

        for i, ch in enumerate(s):
            current += 1
            if ch in lookup:
                current = min(current, i - lookup[ch])
            longest = max(longest, current)
            lookup[ch] = i

        return longest


solution = Solution()
assert solution.lengthOfLongestSubstring("abcabcbb") == 3
assert solution.lengthOfLongestSubstring("bbbbb") == 1
assert solution.lengthOfLongestSubstring("pwwkew") == 3
