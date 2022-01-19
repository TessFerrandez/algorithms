from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert_i = 0
        for i in range(len(nums)):
            if nums[i] != 0 and i != insert_i:
                nums[insert_i] = nums[i]
                nums[i] = 0
            if nums[insert_i] != 0:
                insert_i += 1


solution = Solution()

nums = [0, 1, 0, 3, 12]
solution.moveZeroes(nums)
assert nums == [1, 3, 12, 0, 0]

nums = [0]
solution.moveZeroes(nums)
assert nums == [0]
