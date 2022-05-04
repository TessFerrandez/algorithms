from collections import defaultdict


class Solution:
    # using hash map O(n) O(c)
    def lengthOfLongestSubstring1(self, s: str) -> int:
        longest, start = 0, -1
        last_seen = defaultdict(lambda: -1)

        for i, ch in enumerate(s):
            start = max(start, last_seen[ch])
            last_seen[ch] = i
            longest = max(longest, i - start)

        return longest

    # shrinkable sliding window O(n) O(c)
    def lengthOfLongestSubstring2(self, s: str) -> int:
        n = len(s)
        longest, left = 0, 0
        freq = defaultdict(int)

        def is_invalid():
            return max(freq.values()) > 1

        for right in range(n):
            # update state by adding "right"
            # this might make the window invalid
            freq[s[right]] += 1

            while is_invalid():
                # update state by removing "left"
                freq[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
        return longest

    # shrinkable sliding window (shorter) O(n) O(c)
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        longest = left = duplicate = 0

        for right in range(len(s)):
            freq[s[right]] += 1
            if freq[s[right]] == 2:
                duplicate += 1
            while duplicate > 0:
                freq[s[left]] -= 1
                if freq[s[left]] == 1:
                    duplicate -= 1
                left += 1
            longest = max(longest, right - left + 1)

        return longest


solution = Solution()
assert solution.lengthOfLongestSubstring('abcabcbb') == 3
assert solution.lengthOfLongestSubstring('bbbbb') == 1
assert solution.lengthOfLongestSubstring('pwwkew') == 3
