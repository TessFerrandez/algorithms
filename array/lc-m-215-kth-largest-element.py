'''
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]


solution = Solution()
assert solution.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
assert solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
