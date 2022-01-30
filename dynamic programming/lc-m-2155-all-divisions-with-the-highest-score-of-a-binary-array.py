'''
You are given a 0-indexed binary array nums of length n. nums can be divided at index i (where 0 <= i <= n) into two arrays (possibly empty) numsleft and numsright:

numsleft has all the elements of nums between index 0 and i - 1 (inclusive), while numsright has all the elements of nums between index i and n - 1 (inclusive).
If i == 0, numsleft is empty, while numsright has all the elements of nums.
If i == n, numsleft has all the elements of nums, while numsright is empty.
The division score of an index i is the sum of the number of 0's in numsleft and the number of 1's in numsright.

Return all distinct indices that have the highest possible division score. You may return the answer in any order.
'''
from typing import List


class Solution:
    # the one I submitted
    def maxScoreIndices1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        max_zeros = 0
        zeros = [0] * (n + 1)
        for i, num in enumerate(nums):
            if num == 0:
                max_zeros += 1
            zeros[i + 1] = max_zeros

        max_ones = 0
        ones = [0] * (n + 1)
        ones[-1] = 0
        for i in range(n - 1, -1, -1):
            if nums[i] == 1:
                max_ones += 1
            ones[i] = max_ones

        totals = [ones[i] + zeros[i] for i in range(n + 1)]
        max_total = max(totals)

        return [i for i in range(n + 1) if totals[i] == max_total]

    # optimized
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_ones = sum(nums)

        max_zeros = 0
        max_ones = 0
        totals = [0] * (n + 1)

        for i, num in enumerate(nums):
            totals[i] = max_zeros + (total_ones - max_ones)
            if num == 0:
                max_zeros += 1
            else:
                max_ones += 1

        totals[-1] = max_zeros + (total_ones - max_ones)

        max_total = max(totals)
        return [i for i in range(n + 1) if totals[i] == max_total]


solution = Solution()
assert solution.maxScoreIndices([0, 0, 1, 0]) == [2, 4]
assert solution.maxScoreIndices([0, 0, 0]) == [3]
