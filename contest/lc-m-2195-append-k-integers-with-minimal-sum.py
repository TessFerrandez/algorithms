'''
You are given an integer array nums and an integer k. Append k unique positive integers that do not appear in nums to nums such that the resulting total sum is minimum.

Return the sum of the k integers appended to nums.
'''
from typing import List


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        def ar_sum(low, high):
            return ((high - low + 1) / 2) * (low + high)

        nums.sort()
        last = 0

        min_sum = 0

        for num in nums:
            diff = num - last - 1
            if diff <= 0:
                last = num
                continue
            if diff <= k:
                min_sum += ar_sum(last + 1, num - 1)
                k -= diff
                last = num
            else:
                min_sum += ar_sum(last + 1, last + k)
                return int(min_sum)

        min_sum += ar_sum(last + 1, last + k)
        return int(min_sum)


solution = Solution()
# 3444
print(solution.minimalKSum([26,28,29,32,33,41,43,47,50,53,63,66,71,83,84,88,90], 76))
assert solution.minimalKSum([5, 6], 6) == 25
assert solution.minimalKSum([1, 4, 25, 10, 25], 1) == 2
assert solution.minimalKSum([1, 4, 25, 10, 25], 2) == 5
