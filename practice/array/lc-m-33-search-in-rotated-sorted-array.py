from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        maxn = len(nums) - 1
        low, high = 0, maxn

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] < target:
                if nums[high] < target:
                    high -= 1
                else:
                    low = mid + 1
            elif nums[mid] > target:
                if nums[low] > target:
                    low += 1
                else:
                    high = mid - 1
            else:
                return mid

        return -1


solution = Solution()
assert solution.search([3, 1], 1) == 1
assert solution.search([1, 3, 5], 5) == 2
assert solution.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert solution.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert solution.search([1], 0) == -1
