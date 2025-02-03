# array, two pointers, greedy
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        max_area = min(height[left], height[right]) * (right - left)

        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            max_area = max(max_area, min(height[left], height[right]) * (right - left))

        return max_area


solution = Solution()
assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert solution.maxArea([1, 1]) == 1
assert solution.maxArea([4, 3, 2, 1, 4]) == 16
