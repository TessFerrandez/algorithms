# array, math, two pointers
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            element = nums.pop()
            nums.insert(0, element)

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        [1, 2, 3, 4, 5, 6, 7], 3
        reverse [1, 2, 3, 4, 5, 6, 7] => [7, 6, 5, 4, 3, 2, 1]
        reverse first k elements [5, 6, 7, 4, 3, 2, 1]
        reverse last n-k elements [5, 6, 7, 1, 2, 3, 4]
        """
        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]


solution = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
solution.rotate(nums, 3)
assert(nums == [5, 6, 7, 1, 2, 3, 4])

nums = [-1, -100, 3, 99]
solution.rotate(nums, 2)
assert(nums == [3, 99, -1, -100])

solution = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
solution.rotate2(nums, 3)
assert(nums == [5, 6, 7, 1, 2, 3, 4])

nums = [-1, -100, 3, 99]
solution.rotate2(nums, 2)
assert(nums == [3, 99, -1, -100])
print('All test cases pass')
