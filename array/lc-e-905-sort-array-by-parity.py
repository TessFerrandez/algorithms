'''
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
'''
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        start, end = 0, n - 1
        for num in nums:
            if num % 2 == 0:
                result[start] = num
                start += 1
            else:
                result[end] = num
                end -= 1

        return result


solution = Solution()
assert solution.sortArrayByParity([3, 1, 2, 4]) == [2, 4, 1, 3]
assert solution.sortArrayByParity([0]) == [0]
