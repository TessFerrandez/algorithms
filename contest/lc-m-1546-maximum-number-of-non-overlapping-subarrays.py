from collections import defaultdict
from typing import List


class Solution:
    # my solution - memory limit exceeded
    def maxNonOverlapping1(self, nums: List[int], target: int) -> int:
        def max_disjoint_intervals(intervals):
            if len(intervals) == 0:
                return 0

            count = 1   # first interval is always included
            intervals.sort(key=lambda x: x[1])

            prev_end = intervals[0][1]

            for i in range(1, len(intervals)):
                curr_start = intervals[i][0]
                curr_end = intervals[i][1]

                if curr_start >= prev_end:
                    prev_end = curr_end
                    count += 1

            return count

        prefix_sums = defaultdict(list)

        current = 0
        prefix_sums[0].append(-1)

        for i, num in enumerate(nums):
            current += num
            prefix_sums[current].append(i)

        intervals = []
        for current in prefix_sums:
            diff = current - target
            if diff in prefix_sums:
                for i in prefix_sums[current]:
                    for j in prefix_sums[diff]:
                        if i > j:
                            intervals.append([j, i])

        if intervals == []:
            return 0

        return max_disjoint_intervals(intervals)

    # same idea but greedy
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prefix_sums = {}

        current, count = 0, 0
        prefix_sums[0] = -1

        end = -1
        for i, num in enumerate(nums):
            current += num
            diff = current - target

            if diff in prefix_sums and prefix_sums[diff] >= end:
                count += 1
                end = i

            prefix_sums[current] = i

        return count


solution = Solution()
assert solution.maxNonOverlapping([1, 2, 3, 4], 8) == 0
assert solution.maxNonOverlapping([0, 0, 0], 0) == 3
assert solution.maxNonOverlapping([1,1,1,1,1], 2) == 2
assert solution.maxNonOverlapping([-1,3,5,1,4,2,-9], 6) == 2
