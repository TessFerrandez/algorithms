'''
You are given a 0-indexed integer array nums. Rearrange the values of nums according to the following rules:

Sort the values at odd indices of nums in non-increasing order.
For example, if nums = [4,1,2,3] before this step, it becomes [4,3,2,1] after. The values at odd indices 1 and 3 are sorted in non-increasing order.
Sort the values at even indices of nums in non-decreasing order.
For example, if nums = [4,1,2,3] before this step, it becomes [2,1,4,3] after. The values at even indices 0 and 2 are sorted in non-decreasing order.
Return the array formed after rearranging the values of nums.
'''
from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)

        odd = sorted(nums[::2])
        even = sorted(nums[1::2], reverse=True)

        result = []
        for i in range(n // 2):
            result.append(odd[i])
            result.append(even[i])
        if n % 2:
            result.append(odd[-1])

        return result


solution = Solution()
assert solution.sortEvenOdd([4, 1, 2, 3]) == [2, 3, 4, 1]
assert solution.sortEvenOdd([4, 1, 2, 3, 1]) == [1, 3, 2, 1, 4]
assert solution.sortEvenOdd([2, 1]) == [2, 1]
