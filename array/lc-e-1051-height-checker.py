'''
A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].
'''
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        num_wrong = 0

        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:
                num_wrong += 1

        return num_wrong


solution = Solution()
assert solution.heightChecker([1, 1, 4, 2, 1, 3]) == 3
assert solution.heightChecker([5, 1, 2, 3, 4]) == 5
assert solution.heightChecker([1, 2, 3, 4, 5]) == 0
