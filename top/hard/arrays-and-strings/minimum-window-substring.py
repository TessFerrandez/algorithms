from collections import defaultdict
from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ''

        counts = Counter(t)
        required = len(counts)

        left, right = 0, 0

        # formed = how many unique chars in t are fully present in s
        # fully present => right frequency
        formed = 0
        window_counts = defaultdict(int)

        # window len, left, right
        answer = float('inf'), None, None

        while right < len(s):
            ch = s[right]
            window_counts[ch] += 1

            if ch in counts and window_counts[ch] == counts[ch]:
                formed += 1

            while left <= right and formed == required:
                ch = s[left]

                if right - left + 1 < answer[0]:
                    answer = (right - left + 1, left, right)

                window_counts[ch] -= 1
                if ch in counts and window_counts[ch] < counts[ch]:
                    formed -= 1

                left += 1

            right += 1

        return '' if answer[0] == float('inf') else s[answer[1]: answer[2] + 1]


solution = Solution()
assert solution.minWindow('ADOBECODEBANC', 'ABC') == 'BANC'
assert solution.minWindow('a', 'a') == 'a'
assert solution.minWindow('a', 'aa') == ''
