'''
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
'''
from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative = [num for num in nums if num < 0]
        positive = [num for num in nums if num >= 0]

        result = []
        for i in range(len(positive)):
            result.append(positive[i])
            result.append(negative[i])

        return result


solution = Solution()
assert solution.rearrangeArray([3,1,-2,-5,2,-4]) == [3,-2,1,-5,2,-4]
assert solution.rearrangeArray([-1, 1]) == [1, -1]
