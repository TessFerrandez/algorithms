from functools import cache
from math import inf


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)

        @cache
        def min_len(k, ch, count, idx):
            if k < 0:
                return inf
            if idx == n:
                return 0
            deleteLength = min_len(k - 1, ch, count, idx + 1)
            if ch == s[idx]:
                extra = 1 if (count == 1 or count == 9 or count == 99) else 0
                keepLength = min_len(k, ch, count + 1, idx + 1) + extra
            else:
                keepLength = min_len(k, s[idx], 1, idx + 1) + 1
            return min(deleteLength, keepLength)

        return min_len(k, 0, 0, 0)


solution = Solution()
assert solution.getLengthOfOptimalCompression("aaabcccd", 2) == 4
assert solution.getLengthOfOptimalCompression("aabbaa", 2) == 2
assert solution.getLengthOfOptimalCompression("aaaaaaaaaaa", 0) == 3
