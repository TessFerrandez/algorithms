from bisect import bisect_right
from collections import defaultdict
from typing import List


class Solution:
    # brute force
    def fullBloomFlowers1(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        results = []

        for person in persons:
            count = 0
            for start, end in flowers:
                if start <= person <= end:
                    count += 1
            results.append(count)

        return results

    # recording the start times + binary search
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        times = defaultdict(int)

        # record the interesting times
        for start, end in flowers:
            times[start] += 1
            times[end + 1] -= 1

        sorted_times = [0] + sorted(times.keys())

        # record the number of flowers blooming at a given time
        prefix, blooming = 0, [0]
        for time in sorted_times:
            prefix += times[time]
            blooming.append(prefix)

        # find out how many were blooming when the ppl came
        results = []
        for person in persons:
            time = bisect_right(sorted_times, person)
            results.append(blooming[time])

        return results


solution = Solution()
assert solution.fullBloomFlowers([[1,6],[3,7],[9,12],[4,13]], [2, 3, 7, 11]) == [1, 2, 2, 2]
assert solution.fullBloomFlowers([[1,10],[3,3]], [3, 3, 2]) == [2, 2, 1]
