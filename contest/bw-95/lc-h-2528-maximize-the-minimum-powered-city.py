'''
1. maximize the minimum => binary search is usually a good candidate
2. when validating if a minimum is possible, traverse 0 -> n - 1 to count how many power stations are missing for a given city
3. if x are missing and we have x available - greedily place it as far away to the right as possible (r - 1)
4. if x are missing and we don't have x available - the check fails
'''
from collections import defaultdict
from typing import List


class Solution:
    def maxPower1(self, stations: List[int], r: int, k: int) -> int:
        def possible(stations, n, rng, k, v):
            power = [0 for _ in range(n)]
            power_diffs = [0 for _ in range(n + 1)]

            for idx in range(n):
                power_diffs[max(0, idx - rng)] += stations[idx]
                power_diffs[min(n, idx + rng + 1)] -= stations[idx]

            current_power = 0

            for idx in range(n):
                current_power += power_diffs[idx]
                power[idx] = current_power

            for idx in range(n):
                power_diffs[idx] = 0

            current_power = 0

            for idx in range(n):
                current_power += power_diffs[idx]
                power[idx] += current_power

                if power[idx] >= v:
                    continue

                required = v - power[idx]
                if k < required:
                    return False

                k -= required
                current_power += required
                power_diffs[idx] += required
                power_diffs[min(n, idx + 2 * rng + 1)] -= required

            return True

        low, high = 0, 10 ** 18
        max_power = 0

        while low <= high:
            mid = (low + high) // 2
            if possible(stations, len(stations), r, k, mid):
                max_power = mid
                low = mid + 1
            else:
                high = mid - 1

        return max_power

    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        low, high = min(stations), max(stations) * len(stations) + k    # max possible is sum of all stations + k
        stations = [0] * r + stations + [0] * r                         # adding extras to handle corner cases

        def is_possible(mid):
            available = k
            idx = r                                                     # index of our first city

            window = sum(stations[:2 * r])                              # power of stations for city
            added = defaultdict(int)                                    # which cities have we added stations to?

            while idx < len(stations) - r:
                window += stations[idx + r]

                if window < mid:
                    diff = mid - window
                    if diff > available:
                        return False
                    window += diff
                    added[idx + r] = diff
                    available -= diff

                window -= (stations[idx - r] + added[idx - r])
                idx += 1

            return True

        min_max_power = low

        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid):
                min_max_power = mid
                low = mid + 1
            else:
                high = mid - 1

        return min_max_power


solution = Solution()
assert solution.maxPower([1, 2, 4, 5, 0], 1, 2) == 5
assert solution.maxPower([4, 4, 4, 4], 0, 3) == 4
