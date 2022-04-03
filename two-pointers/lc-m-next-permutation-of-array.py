from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        '''
        if all are in descending order, we can't do better so return reverse
        '''
        def reverse(nums, start):
            i, j = start, len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        i = len(nums) - 2

        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        reverse(nums, i + 1)


solution = Solution()

arr = [3, 2, 1]
solution.nextPermutation(arr)
assert arr == [1, 2, 3]

arr = [1, 2, 3]
solution.nextPermutation(arr)
assert arr == [1, 3, 2]

arr = [1, 1, 5]
solution.nextPermutation(arr)
assert arr == [1, 5, 1]
