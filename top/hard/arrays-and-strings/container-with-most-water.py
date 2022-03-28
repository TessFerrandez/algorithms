from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        n = len(height)
        max_area = 0

        while left < right:
            width = right - left

            area = min(height[left], height[right]) * width
            max_area = max(area, max_area)

            if height[left] < height[right]:
                while left + 1 <= n - 1 and height[left + 1] <= height[left]:
                    left += 1
                left += 1
            else:
                while right - 1 >= 0 and height[right - 1] <= height[right]:
                    right -= 1
                right -= 1

        return max_area


solution = Solution()
assert solution.maxArea([1,8,6,2,5,4,8,3,7]) == 49
assert solution.maxArea([1, 1]) == 1
assert solution.maxArea([3, 9, 3, 4, 7, 2, 12, 6]) == 45
