from collections import Counter
from math import inf


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        start - end represents a window
        1. move end to find a valid window
        2. when we have a valid window, move start to find a smaller window
        '''
        map = Counter(t)
        counter = len(t)
        start, end, min_start, min_len = 0, 0, 0, inf

        while end < len(s):
            # if ch in t - decrease counter
            if map[s[end]] > 0:
                counter -= 1

            # if ch was not in t - map[s[end]] will be negative
            map[s[end]] -= 1
            end += 1

            # when we find a valid window
            # move start to find a smaller window
            while counter == 0:
                if end - start < min_len:
                    min_start = start
                    min_len = end - start
                map[s[start]] += 1
                # when the ch exists in t, increase counter
                if map[s[start]] > 0:
                    counter += 1
                start += 1

        if min_len != inf:
            return s[min_start: min_start + min_len]
        return ''


solution = Solution()
assert solution.minWindow("ADOBECODEBANC", "ABC") == "BANC"
assert solution.minWindow("a", "a") == "a"
assert solution.minWindow("a", "aa") == ""
