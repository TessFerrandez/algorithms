from collections import defaultdict
from math import inf


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        n = len(s)
        start, longest, max_char_count = 0, -inf, 0

        for end in range(n):
            # grow until we are no good
            right_char = s[end]
            freq[right_char] += 1

            max_char_count = max(max_char_count, freq[right_char])

            # shrink until we're good
            while ((end - start + 1) - max_char_count) > k:
                left_char = s[start]
                freq[left_char] -= 1
                start += 1

            longest = max(longest, end - start + 1)

        return longest


solution = Solution()
assert solution.characterReplacement('ABAB', 2) == 4
assert solution.characterReplacement('AABABBA', 1) == 4
