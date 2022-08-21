from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last = {}

        day = 0
        for task in tasks:
            if task not in last:
                day += 1
                last[task] = day
            else:
                day = max(day + 1, last[task] + space + 1)
                last[task] = day

        return day


solution = Solution()
assert solution.taskSchedulerII([1,2,1,2,3,1], 3) == 9
assert solution.taskSchedulerII([5,8,8,5], 2) == 6
assert solution.taskSchedulerII([4, 10, 10, 9, 10, 10, 4], 8) == 30
