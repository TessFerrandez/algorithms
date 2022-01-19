'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
---
Water trapped at a given i is min(left_max, right_max) - height[i]
Sum is the sum of all water trapped
'''
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0

        left_max = [0 for _ in range(len(height))]
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max = [0 for _ in range(len(height))]
        right_max[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        return sum(min(left_max[i], right_max[i]) - height[i] for i in range(len(height)))


solution = Solution()
assert solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert solution.trap([4, 2, 0, 3, 2, 5]) == 9
