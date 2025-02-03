# array, two pointers
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current_index = 0
        elements = set()

        for element in nums:
            if element not in elements:
                elements.add(element)
                nums[current_index] = element
                current_index += 1

        return current_index


solution = Solution()
nums = [1, 1, 2]
assert(solution.removeDuplicates(nums) == 2)
assert(nums[:2] == [1, 2])

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
assert(solution.removeDuplicates(nums) == 5)
assert(nums[:5] == [0, 1, 2, 3, 4])
print('All test cases pass')
