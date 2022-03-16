from typing import List
from collections import Counter


class Solution:
    # count sort
    def sortColors1(self, nums: List[int]) -> None:
        counts = Counter(nums)

        j = 0
        for i in range(3):
            for _ in range(counts[i]):
                nums[j] = i
                j += 1

    # dutch positioning
    def sortColors(self, nums):
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1


solution = Solution()

nums = [2, 0, 2, 1, 1, 0]
solution.sortColors(nums)
assert nums == [0, 0, 1, 1, 2, 2]

nums = [2, 0, 1]
solution.sortColors(nums)
assert nums == [0, 1, 2]
