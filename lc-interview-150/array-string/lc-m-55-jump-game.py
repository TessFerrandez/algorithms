# array, dynamic programming, greedy
from functools import cache
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @cache
        def can_jump_from(position: int) -> bool:
            if position == len(nums) - 1:
                return True

            furthest_jump = min(position + nums[position], len(nums) - 1)
            for next_position in range(position + 1, furthest_jump + 1):
                if can_jump_from(next_position):
                    return True

            return False

        return can_jump_from(0)


solution = Solution()
assert(solution.canJump([2, 3, 1, 1, 4]))
assert(not solution.canJump([3, 2, 1, 0, 4]))
