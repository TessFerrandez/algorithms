from functools import cache
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def max_strings(i, zeros, ones):
            if i < 0:
                return 0

            i0s, i1s = strs[i].count('0'), strs[i].count('1')
            pick_i = 0 if i0s > zeros or i1s > ones else 1 + max_strings(i - 1, zeros - i0s, ones - i1s)
            dont_pick_i = max_strings(i - 1, zeros, ones)
            return max(pick_i, dont_pick_i)

        return max_strings(len(strs) - 1, m, n)


solution = Solution()
assert solution.findMaxForm(["10","0001","111001","1","0"], 5, 3) == 4
assert solution.findMaxForm(["10","0","1"], 1, 1) == 2
