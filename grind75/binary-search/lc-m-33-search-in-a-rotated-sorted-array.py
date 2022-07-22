from bisect import bisect_left
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        def find_pivot():
            if n == 1:
                return 0

            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if mid < high and nums[mid] > nums[mid + 1]:
                    return mid + 1
                if mid > low and nums[mid] < nums[mid - 1]:
                    return mid
                if nums[low] >= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # we can't find pivot
            return n

        pivot = find_pivot()
        nums = nums[pivot:] + nums[: pivot]
        pos = bisect_left(nums, target)

        if pos >= n:
            return -1
        if nums[pos] != target:
            return -1
        return (pos + pivot) % n


solution = Solution()
assert solution.search([3, 1], 3) == 0
assert solution.search([1], 2) == -1
assert solution.search([1,2,4,5,6,7,0], 0) == 6
assert solution.search([0,1,2,4,5,6,7], 0) == 0
assert solution.search([1], 1) == 0
assert solution.search([4,5,6,7,0,1,2], 0) == 4
assert solution.search([4,5,6,7,0,1,2], 3) == -1
assert solution.search([1], 0) == -1
