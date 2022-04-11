from typing import List


class Solution:
    # one pass but a bit slower
    def isMonotonic1(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        pos = True
        neg = True
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                pos = False
            if nums[i - 1] < nums[i]:
                neg = False

        if pos or neg:
            return True

        return False

    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        pos = True
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                pos = False
                break
        if pos:
            return True

        neg = True
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                neg = False
                break
        if neg:
            return True

        return False


solution = Solution()
assert solution.isMonotonic([1, 1, 2, 2, 3])
assert solution.isMonotonic([1, 2, 2, 3])
assert solution.isMonotonic([6, 5, 4, 4])
assert not solution.isMonotonic([1, 3, 2])
