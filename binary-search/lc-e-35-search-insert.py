from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num >= target:
                return i

        return len(nums)

    def searchInsert2(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)

        while low < high:
            mid = low + ((high - low) // 2)

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid

        return low


solution = Solution()
assert solution.searchInsert([1,3,5,6], 5) == 2
assert solution.searchInsert([1,3,5,6], 2) == 1
assert solution.searchInsert([1,3,5,6], 7) == 4
