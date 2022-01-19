from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if num == target:
                return i
            if num > target:
                return -1

        return -1


solution = Solution()
print(solution.search([-1, 0, 3, 5, 9, 12], 9))
print(solution.search([-1, 0, 3, 5, 9, 12], 2))
