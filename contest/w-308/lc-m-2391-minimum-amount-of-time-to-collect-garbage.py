from collections import defaultdict
from itertools import accumulate
from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        prefix = [0] + list(accumulate(travel))
        total_garbage = 0
        last_garbage = defaultdict(int)

        for house, garbages in enumerate(garbage):
            for garbage_type in garbages:
                last_garbage[garbage_type] = house
            total_garbage += len(garbages)

        for garbage_type in last_garbage:
            total_garbage += prefix[last_garbage[garbage_type]]

        return total_garbage


solution = Solution()
assert solution.garbageCollection(["G","P","GP","GG"], [2,4,3]) == 21
assert solution.garbageCollection(["MMM","PGM","GP"], [3,10]) == 37
