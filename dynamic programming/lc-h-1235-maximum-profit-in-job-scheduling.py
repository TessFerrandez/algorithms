from bisect import bisect_left
from collections import defaultdict, deque
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        max_profit = defaultdict(int)
        start_times = deque([])

        jobs = list(zip(startTime, endTime, profit))
        jobs.sort(reverse=True)

        for start, end, salary in jobs:
            n = len(start_times)
            if not start_times:
                max_profit[start] = salary
            else:
                current = 0

                first_after_start = bisect_left(start_times, start)
                if first_after_start < n:
                    # best could be if we skipped this one
                    current = max(current, max_profit[start_times[first_after_start]])

                first_after_end = bisect_left(start_times, end)
                if first_after_end < n:
                    best_after = max_profit[start_times[first_after_end]]
                else:
                    best_after = 0
                current = max(current, salary + best_after)
                max_profit[start] = current

            if not start_times or start_times[0] != start:
                start_times.appendleft(start)

        return max_profit[start_times[0]]


solution = Solution()
assert solution.jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]) == 120
assert solution.jobScheduling([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]) == 150
assert solution.jobScheduling([1, 1, 1], [2, 3, 4], [5, 6, 4]) == 6
