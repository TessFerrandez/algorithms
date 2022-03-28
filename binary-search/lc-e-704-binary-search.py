from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1


solution = Solution()
assert solution.search([-1, 0, 3, 5, 9, 12], 9) == 4
assert solution.search([-1, 0, 3, 5, 9, 12], 2) == -1
