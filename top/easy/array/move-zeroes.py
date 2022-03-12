from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert = 0
        zeros = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                nums[insert] = nums[i]
                insert += 1

        for _ in range(zeros):
            nums[insert] = 0
            insert += 1


solution = Solution()

arr = [0, 1, 0, 3, 12]
solution.moveZeroes(arr)
assert arr == [1, 3, 12, 0, 0]

arr = [0]
solution.moveZeroes(arr)
assert arr == [0]
