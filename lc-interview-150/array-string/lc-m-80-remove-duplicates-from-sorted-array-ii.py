from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current_index = 0

        for element in nums:
            if current_index < 2 or element != nums[current_index - 2]:
                nums[current_index] = element
                current_index += 1

        return current_index


solution = Solution()
nums = [1, 1, 1, 2, 2, 3]
assert(solution.removeDuplicates(nums) == 5)
assert(nums[:5] == [1, 1, 2, 2, 3])

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
assert(solution.removeDuplicates(nums) == 7)
assert(nums[:7] == [0, 0, 1, 1, 2, 3, 3])
