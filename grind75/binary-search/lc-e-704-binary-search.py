from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1

        return low if nums[low] == target else -1


solution = Solution()
solution.search([-1, 0, 3, 4, 9, 12], 9) == 4
solution.search([-1, 0, 3, 5, 9, 12], 2) == -1
