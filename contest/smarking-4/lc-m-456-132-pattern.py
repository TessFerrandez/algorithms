from math import inf
from typing import List


'''
i < j < k
nums[i] < nums[k] < nums[j]
'''
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        second = -inf

        # numbers in decreasing order
        descending = []

        for num in nums[::-1]:
            if num < second:
                return True

            while descending and descending[-1] < num:
                second = descending.pop()

            descending.append(num)

        return False


solution = Solution()
assert not solution.find132pattern([1, 2, 3, 4])
assert solution.find132pattern([3, 1, 4, 2])
assert solution.find132pattern([-1, 3, 2, 0])
