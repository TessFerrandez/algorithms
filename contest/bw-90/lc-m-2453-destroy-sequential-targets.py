from cmath import inf
from collections import defaultdict
from typing import List


class Solution:
    # my solution in competition
    def destroyTargets1(self, nums: List[int], space: int) -> int:
        nums.sort()

        mod_count = defaultdict(int)
        mod_first = {}

        best_count = 0
        best_mod = -1

        for num in nums:
            remainder = num % space
            mod_count[remainder] += 1
            if remainder not in mod_first:
                mod_first[remainder] = num

            if mod_count[remainder] > best_count:
                best_count = mod_count[remainder]
                best_mod = remainder
            elif mod_count[remainder] == best_count:
                if mod_first[best_mod] > mod_first[remainder]:
                    best_mod = remainder

        return mod_first[best_mod]

    def destroyTargets(self, nums: List[int], space: int) -> int:
        remainders = defaultdict(lambda: (0, inf))
        max_count = 0

        for num in nums:
            remainder = num % space
            count, min_num = remainders[remainder]

            count += 1
            min_num = min(min_num, num)

            remainders[remainder] = (count, min_num)
            max_count = max(max_count, count)

        result = inf
        for count, min_num in remainders.values():
            if count == max_count:
                result = min(result, min_num)

        return result


solution = Solution()
assert solution.destroyTargets([625879766,235326233,250224393,501422042,683823101,948619719,680305710,733191937,182186779,353350082], 4) == 235326233
assert solution.destroyTargets([3,7,8,1,1,5], 2) == 1
assert solution.destroyTargets([1,3,5,2,4,6], 2) == 1
assert solution.destroyTargets([6,2,5], 100) == 2
