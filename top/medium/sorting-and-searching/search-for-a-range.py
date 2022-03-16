from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1

        for i, num in enumerate(nums):
            if num == target and start == -1:
                start = i
            if num > target:
                if start != -1:
                    return [start, i - 1]

        if start != -1:
            return [start, len(nums) - 1]

        return [-1, -1]


solution = Solution()
assert solution.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
assert solution.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
assert solution.searchRange([], 0) == [-1, -1]
