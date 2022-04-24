from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        def find_pivot():
            left, right = 0, len(nums) - 1

            if right == left:
                return left

            while left <= right:
                mid = (left + right) // 2
                if mid < right and nums[mid] > nums[mid + 1]:
                    return mid
                if mid > left and nums[mid] < nums[mid - 1]:
                    return mid - 1

                if nums[left] >= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            return len(nums) - 1

        pivot = find_pivot()
        lowest_i = (pivot + 1) % (len(nums))
        return nums[lowest_i]


solution = Solution()
assert solution.findMin([3, 4, 5, 1, 2]) == 1
assert solution.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
