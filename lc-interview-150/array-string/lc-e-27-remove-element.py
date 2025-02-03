# array, two pointers
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        current_index = 0

        for element in nums[:]:
            if element != val:
                nums[current_index] = element
                current_index += 1

        return current_index


solution = Solution()
nums = [3, 2, 2, 3]
assert(solution.removeElement(nums, 3) == 2)
assert(nums[:2] == [2, 2])

nums = [0, 1, 2, 2, 3, 0, 4, 2]
assert(solution.removeElement(nums, 2) == 5)
assert(nums[:5] == [0, 1, 3, 0, 4])
