class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        char_index = {}

        for right, char in enumerate(s):
            if char not in char_index or char_index[char] < left:
                char_index[char] = right
                longest = max(longest, right - left + 1)
            else:
                left = char_index[char] + 1
                char_index[char] = right

        return longest


solution = Solution()
assert solution.lengthOfLongestSubstring('abcabcbb') == 3
assert solution.lengthOfLongestSubstring('bbbbb') == 1
assert solution.lengthOfLongestSubstring('pwwkew') == 3
