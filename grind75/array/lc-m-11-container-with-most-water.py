from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        best = 0
        while left < right:
            current = (right - left) * min(height[left], height[right])
            best = max(best, current)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return best


solution = Solution()
assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert solution.maxArea([1, 1]) == 1
