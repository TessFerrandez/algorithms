# array, dynamic programming, greedy
from functools import cache
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        last_position = len(nums) - 1

        @cache
        def min_steps_from(position):
            if position == last_position:
                return 0
            max_jump_to = min(position + nums[position], last_position)
            min_steps = []
            for next_position in range(position + 1, max_jump_to + 1):
                min_steps.append(min_steps_from(next_position))
            if min_steps:
                return 1 + min(min_steps)
            return float('inf')

        return min_steps_from(0)


solution = Solution()
assert(solution.jump([2, 3, 1, 1, 4]) == 2)
assert(solution.jump([2, 3, 0, 1, 4]) == 2)
