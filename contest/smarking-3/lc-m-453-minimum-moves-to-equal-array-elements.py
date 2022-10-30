from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)


solution = Solution()
assert solution.minMoves([1, 2, 3]) == 3
assert solution.minMoves([1, 1, 1]) == 0
