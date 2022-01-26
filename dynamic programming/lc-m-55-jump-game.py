'''
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Ex. [2, 3, 1, 1, 4]
dp[0] is true if one of [1, 2] is true
dp[1] is true if one of [2, 3, 4] is true
dp[2] is true if one of [3] is true
dp[3] is true if one of [4] is true
dp[4] is true (last index)

find dp[0]
'''
from typing import List

class Solution:
    # my solution
    def canJump2(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False for _ in range(n)]
        dp[n - 1] = True

        for i in range(n - 2, -1, -1):
            for nx in range(i + 1, min(i + nums[i] + 1, n)):
                if dp[nx] == True:
                    dp[i] = True
                    break

        return dp[0]

    def canJump(self, nums: List[int]) -> bool:
        '''
        O(n) solution -- keep track of the smallest index that can jump to the end
        and check if current index can jump to this smallest index

        23114
        i   last    new_last
        3   4       3 + 1 >= 4 => 3
        2   3       2 + 1 >= 3 => 2
        1   2       1 + 3 >= 2 => 1
        0   1       0 + 2 >= 1 => 0 so True
        '''
        n = len(nums)
        last = n - 1

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= last:
                last = i

        return last <= 0


solution = Solution()
assert solution.canJump([2, 3, 1, 1, 4]) == True
assert solution.canJump([3, 2, 1, 0, 4]) == False
