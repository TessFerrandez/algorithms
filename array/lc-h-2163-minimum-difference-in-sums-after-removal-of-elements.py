'''
You are given a 0-indexed integer array nums consisting of 3 * n elements.

You are allowed to remove any subsequence of elements of size exactly n from nums. The remaining 2 * n elements will be divided into two equal parts:

The first n elements belonging to the first part and their sum is sumfirst.
The next n elements belonging to the second part and their sum is sumsecond.
The difference in sums of the two parts is denoted as sumfirst - sumsecond.

For example, if sumfirst = 3 and sumsecond = 2, their difference is 1.
Similarly, if sumfirst = 2 and sumsecond = 3, their difference is -1.
Return the minimum difference possible between the sums of the two parts after the removal of n elements.

----------------
Algo from Bakerston

first will be the n numbers with the smallest sum from index 0 -> len - n
second will be the n numbers with the highest sum from index n -> len


Ex: n = 3
            3  5  2  2  1  7 | 3 6 1
min_left    -  - 10  7  5  5

            3  5  2 | 2  1  7  3  6  1
max_right             16 16 16 10 -  -

min_left -  10  7   5   5
max_right   16  16  16  10
            -6  -9  -11 -5 ==> -11
'''
from typing import List
from heapq import heappop, heappush, heapify
import math


class Solution:
    # solution based on Bakerston idea
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        # Build pre_min using min-heap.
        pre_min, cur_min = [sum(nums[:n])], sum(nums[:n])
        pre_hp = [-num for num in nums[:n]]
        heapify(pre_hp)

        for i in range(n, 2 * n):
            cur_pop = -heappop(pre_hp)
            cur_min -= cur_pop
            cur_min += min(cur_pop, nums[i])
            pre_min.append(cur_min)
            heappush(pre_hp, -min(cur_pop, nums[i]))

        # Build suf_max.
        suf_max, cur_max = [sum(nums[2 * n:])], sum(nums[2 * n:])
        suf_hp = [num for num in nums[2 * n:]]
        heapify(suf_hp)

        for i in range(2 * n - 1, n - 1, -1):
            cur_pop = heappop(suf_hp)
            cur_max -= cur_pop
            cur_max += max(cur_pop, nums[i])
            suf_max.append(cur_max)
            heappush(suf_hp, max(cur_pop, nums[i]))

        suf_max = suf_max[::-1]

        # Iterate over pre_min and suf_max and get the minimum difference.
        min_diff = math.inf

        for pmin, smax in zip(pre_min, suf_max):
            min_diff = min(min_diff, pmin - smax)

        return min_diff


solution = Solution()
assert solution.minimumDifference([3, 5, 2, 2, 1, 7, 3, 6, 1]) == -11
assert solution.minimumDifference([16, 46, 43, 41, 42, 14, 36, 49, 50, 28, 38, 25, 17, 5, 18, 11, 14, 21, 23, 39, 23]) == -14
assert solution.minimumDifference([3, 1, 2]) == -1
assert solution.minimumDifference([7, 9, 5, 8, 1, 3]) == 1
