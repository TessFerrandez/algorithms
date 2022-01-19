from typing import List


class Solution:
    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        rotated = nums[-k:]
        for i in range(len(nums) - k - 1, -1, -1):
            nums[i + k] = nums[i]
        for i in range(len(rotated)):
            nums[i] = rotated[i]

    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            n = nums.pop()
            nums.insert(0, n)


solution = Solution()

nums = [1,2,3,4,5,6,7]
solution.rotate(nums, 3)
assert nums == [5,6,7,1,2,3,4]