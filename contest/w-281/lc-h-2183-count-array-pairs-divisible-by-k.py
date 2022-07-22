from typing import List
from collections import defaultdict
from math import comb, gcd


class Solution:
    # TLE
    def countPairs_tle(self, nums: List[int], k: int) -> int:
        max_divisor = 0
        gcds = defaultdict(list)
        gcd_lookup = []

        for i, num in enumerate(nums):
            the_gcd = gcd(num, k)
            max_divisor = max(max_divisor, the_gcd)
            gcds[the_gcd].append(i)
            gcd_lookup.append(the_gcd)

        pairs = 0
        for i, d in enumerate(gcd_lookup):
            divisor = k // d
            times = 1
            while times * divisor <= max_divisor:
                possible = gcds[times * divisor]
                pairs += sum(1 for p in possible if p > i)
                times += 1

        return pairs

    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count_gcd = defaultdict(int)
        divisor_target = defaultdict(set)

        # build counts of greatest common divisors and their 'targets'
        for num in nums:
            g = gcd(num, k)
            if g == k:
                count_gcd[k] += 1
            elif g == 1:
                pass
            else:
                count_gcd[g] += 1
                target = k // g
                divisor_target[target].add(g)

        pairs = 0

        # check for those that directly divide with k
        if count_gcd[k] > 0:
            nk = count_gcd[k]
            count_gcd.pop(k)
            pairs += (n - nk) * nk + comb(nk, 2)

        # check for pairs - saving away those we already visited
        # so we don't double count
        visited = set()
        for target in divisor_target:
            for g in divisor_target[target]:
                # fetch gcd counts that need to pair with target
                ng = count_gcd[g]
                # check the presense of target, 2 * target, 3 * target...
                for target_multiplier in range(target, k, target):
                    if target_multiplier in count_gcd and (g, target_multiplier) not in visited:
                        visited.add((g, target_multiplier))
                        visited.add((target_multiplier, g))
                        if target_multiplier != g:
                            pairs += ng * count_gcd[target_multiplier]
                        else:
                            # in case target == g == sqrt(k)
                            pairs += comb(ng, 2)

        return pairs


solution = Solution()
assert solution.countPairs([2, 6, 8, 10], 12) == 3
assert solution.countPairs([1, 2, 3, 4, 5], 2) == 7
assert solution.countPairs([1, 2, 3, 4], 5) == 0
assert solution.countPairs(list(range(1, 100001)), 1) == 4999950000
