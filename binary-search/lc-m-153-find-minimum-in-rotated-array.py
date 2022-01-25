'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

ALGO:
--------------------
Ex [4 5 6 7 | 2 3]

We want to find the | point - the point where both the item to the left and to the right is higher
'''
from typing import List


class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]

        left, right = 0, n - 1

        # if first is smaller than last
        # it's already sorted so first is lowest
        if nums[right] > nums[0]:
            return nums[0]

        while right >= left:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1


solution = Solution()
assert solution.findMin([3,4,5,1,2]) == 1
assert solution.findMin([4,5,6,7,0,1,2]) == 0
assert solution.findMin([11,13,15,17]) == 11
