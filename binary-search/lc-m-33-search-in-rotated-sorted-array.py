'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1

        rotate_pos = 0
        for i in range(1, n):
            if nums[i] == target:
                return i
            if nums[i] < nums[i - 1]:
                nums = nums[i:] + nums[:i]
                rotate_pos = i
                break

        low, high = 0, n -1
        while low <= high:
            mid = (high - low) // 2 + low
            if nums[mid] == target:
                return (mid + rotate_pos) % n
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1


solution = Solution()
assert solution.search([1, 3], 1) == 0
assert solution.search([4,5,6,7,0,1,2], 0) == 4
assert solution.search([4,5,6,7,0,1,2], 3) == -1
assert solution.search([1], 0) == -1
