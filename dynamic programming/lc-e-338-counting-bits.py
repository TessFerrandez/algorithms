'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
'''
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        dp = [0, 1]

        p = 2
        idx = 0

        for i in range(2, n + 1):
            if i == 2 ** p:
                idx = 0
                p += 1
            dp.append(dp[idx] + 1)
            idx += 1

        return dp


solution = Solution()
assert solution.countBits(0) == [0]
assert solution.countBits(2) == [0, 1, 1]
assert solution.countBits(5) == [0, 1, 1, 2, 1, 2]
