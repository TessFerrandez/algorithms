from bisect import bisect_left
from typing import List


class Solution:
    # my solution
    # T O(m log m + n log m)
    # S O(n)
    def successfulPairs1(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)

        result = []
        for spell in spells:
            needed = success / spell
            num_ok = n - bisect_left(potions, needed)
            result.append(num_ok)

        return result


solution = Solution()
assert solution.successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7) == [4, 0, 3]
assert solution.successfulPairs([3, 1, 2], [8, 5, 8], 16) == [2, 0, 2]
