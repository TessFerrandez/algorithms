# array, two pointers, dynamic programming, stack, monotonic stack
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0]
        max_right = [0]

        for curr_height in height:
            max_left.append(max(max_left[-1], curr_height))
        max_left = max_left[1:]

        for curr_height in height[::-1]:
            max_right.append(max(max_right[-1], curr_height))
        max_right = max_right[1:][::-1]

        bounds = [min(left, right) for left, right in zip(max_left, max_right)]
        return sum([bound - curr_height for bound, curr_height in zip(bounds, height)])


solution = Solution()
assert solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert solution.trap([4, 2, 0, 3, 2, 5]) == 9
