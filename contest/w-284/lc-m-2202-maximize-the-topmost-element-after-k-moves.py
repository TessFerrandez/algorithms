'''
You are given a 0-indexed integer array nums representing the contents of a pile, where nums[0] is the topmost element of the pile.

In one move, you can perform either of the following:

If the pile is not empty, remove the topmost element of the pile.
If there are one or more removed elements, add any one of them back onto the pile. This element becomes the new topmost element.
You are also given an integer k, which denotes the total number of moves to be made.

Return the maximum value of the topmost element of the pile possible after exactly k moves. In case it is not possible to obtain a non-empty pile after k moves, return -1.
'''
from typing import List


class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if n == 1:
            if k % 2 == 0:
                # just keep removing and adding the same number
                return nums[0]
            return -1

        if k <= 1:
            return nums[k]

        if k > n:
            return max(nums)

        if k == n:
            return max(nums[:k - 1])
        else:
            return max(max(nums[:k - 1]), nums[k])


solution = Solution()
assert solution.maximumTop([4,6,1,0,6,2,4], 0) == 4
assert solution.maximumTop([100, 9, 6, 8, 7], 5) == 100
assert solution.maximumTop([68,76,53,73,85,87,58,24,48,59,38,80,38,65,90,38,45,22,3,28,11], 1) == 76
assert solution.maximumTop([5,2,2,4,0,6], 4) == 5
assert solution.maximumTop([2], 1) == -1
