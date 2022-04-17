from typing import List


class Solution:
    def specialArray1(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i = 0
        while i < len(nums) and nums[i] > i:
            i += 1
        return -1 if i < len(nums) and i == nums[i] else i

    # with binary search
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        low, high = 0, len(nums)

        while low < high:
            mid = (low + high) // 2
            if mid < nums[mid]:
                low = mid + 1
            else:
                high = mid

        return -1 if low < len(nums) and low == nums[low] else low


solution = Solution()
assert solution.specialArray([3, 5]) == 2
assert solution.specialArray([0, 0]) == -1
assert solution.specialArray([0, 4, 3, 0, 4]) == 3
