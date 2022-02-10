'''
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

ALGO:
The sum of a subarray [i, j] = sum[0, j] - sum[0, i - 1]
ex.

idx     0   1   2   3   4   5   6
        1, -1,  1, -1,  1,  3,  2

Sum of 3->5 = -1 + 1 + 3 = 3
Sum[2] = 1 - 1 + 1 = 1
Sum[5] = 1 - 1 + 1 - 1 + 1 + 3 = 4
Sum[3 -> 5] = Sum[5] - Sum[2] = 3

So for any given j -- check how many starts we have, i.e. how many ways we can get to k - Sum[j]
Easiest way is to keep recording the number of indices that end in each sum
'''
from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        sums[0] = 1

        num_sums = 0
        current_sum = 0

        for num in nums:
            current_sum += num
            if current_sum - k in sums:
                num_sums += sums[current_sum - k]
            sums[current_sum] += 1

        return num_sums


solution = Solution()
assert solution.subarraySum([1, 1, 1], 2) == 2
assert solution.subarraySum([1, 2, 3], 3) == 2
assert solution.subarraySum([1, -1, 1, -1, 1, 3, 2], 3) == 3
