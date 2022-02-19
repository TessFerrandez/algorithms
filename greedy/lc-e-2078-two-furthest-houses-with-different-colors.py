'''
There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.

Return the maximum distance between two houses with different colors.

The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.
'''
from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        start, end = 0, len(colors) - 1

        # from the start
        while colors[end] == colors[start]:
            end -= 1
        max_distance = end - start

        # from the end
        end = len(colors) - 1
        while colors[start] == colors[end]:
            start += 1
        max_distance = max(max_distance, end - start)

        return max_distance


solution = Solution()
assert solution.maxDistance([1, 1, 1, 6, 1, 1, 1]) == 3
assert solution.maxDistance([1, 8, 3, 8, 3]) == 4
assert solution.maxDistance([0, 1]) == 1
