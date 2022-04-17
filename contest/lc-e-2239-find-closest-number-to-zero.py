from typing import List


class Solution:
    # my solution - using binary search
    def findClosestNumber1(self, nums: List[int]) -> int:
        def searchInsert(nums: List[int], target: int) -> int:
            low, high = 0, len(nums)

            while low < high:
                mid = (low + high) // 2

                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid

            return low

        nums.sort()
        i = searchInsert(nums, 0)
        if i == 0:
            return nums[i]
        if i == len(nums):
            return nums[-1]
        if abs(0 - nums[i - 1]) < abs(nums[i]):
            return nums[i - 1]
        return nums[i]

    # simple solution
    def findClosestNumber(self, nums: List[int]) -> int:
        best_dist, best_num = abs(nums[0]), nums[0]
        for num in nums:
            if abs(num) < best_dist:
                best_dist = abs(num)
                best_num = num
            if abs(num) == best_dist:
                best_num = max(num, best_num)

        return best_num


solution = Solution()
assert solution.findClosestNumber([-4,-2,1,4,8]) == 1
assert solution.findClosestNumber([2, -1, 1]) == 1
