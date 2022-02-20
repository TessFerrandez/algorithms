'''
Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.
'''
from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)

        if total % 3 != 0:
            return False

        parts = 0
        part_sum = total // 3

        cum_sum = 0
        for num in arr:
            cum_sum += num
            if cum_sum == part_sum:
                cum_sum = 0
                parts += 1

        return parts >= 3


solution = Solution()
assert solution.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1])
assert not solution.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1])
assert solution.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4])
assert solution.canThreePartsEqualSum([0, 0, 0, 0])
