'''
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment n - 1 elements of the array by 1.

initial_sum + moves * (n - 1) = end_num * n

since lowest number needs to increase all the time:
end_num = min_num + moves

so:
initial_sum + moves * (n - 1) = (min_num + moves) * n
initial_sum + moves * n - moves = min_num * n + moves * n
initial_sum - min_num * n = moves
'''
from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - min(nums) * len(nums)


solution = Solution()
assert solution.minMoves([1, 2, 3]) == 3
assert solution.minMoves([1, 1, 1]) == 0
