'''
Given the array nums, obtain a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements in such subsequence.

If there are multiple solutions, return the subsequence with minimum size and if there still exist multiple solutions, return the subsequence with the maximum total sum of all its elements. A subsequence of an array can be obtained by erasing some (possibly zero) elements from the array.

Note that the solution with the given constraints is guaranteed to be unique. Also return the answer sorted in non-increasing order.
'''
from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        other_sum = sum(nums)
        subsequence_sum = 0

        subsequence = []

        for num in nums:
            other_sum -= num
            subsequence_sum += num
            subsequence.append(num)
            if subsequence_sum > other_sum:
                return subsequence

        return []


solution = Solution()
assert solution.minSubsequence([4, 3, 10, 9, 8]) == [10, 9]
assert solution.minSubsequence([4, 4, 7, 6, 7]) == [7, 7, 6]
assert solution.minSubsequence([6]) == [6]
