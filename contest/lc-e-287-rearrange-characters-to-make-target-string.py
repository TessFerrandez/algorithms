from collections import Counter
from math import inf


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        target_count = Counter(target)
        available_count = Counter(s)

        times = inf
        for ch in target_count:
            times = min(times, available_count[ch] // target_count[ch])

        return times


solution = Solution()
assert solution.rearrangeCharacters("ilovecodingonleetcode", "code") == 2
assert solution.rearrangeCharacters("abcba", "abc") == 1
assert solution.rearrangeCharacters("abbaccaddaeea", "aaaaa") == 1
