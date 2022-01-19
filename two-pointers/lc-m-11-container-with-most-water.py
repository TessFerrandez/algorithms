'''
Given an array of water heights,
find 2 lines, that together with the x-axis
form a container such that the container contains
the most water

Algorithm:
--------------------------
starting with the container at the outer lines
continuously move the lower one in - and if you find
higher bar, use that
'''
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        start = 0
        end = len(height) - 1

        while start < end:
            max_area = max(max_area, min(height[start], height[end]) * (end - start))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_area


solution = Solution()
assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert solution.maxArea([3, 9, 3, 4, 7, 2, 12, 6]) == 45
