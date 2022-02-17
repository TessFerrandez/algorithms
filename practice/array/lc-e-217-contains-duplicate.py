from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


solution = Solution()
assert solution.containsDuplicate([1, 2, 3, 1])
assert not solution.containsDuplicate([1, 2, 3, 4])
assert solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
