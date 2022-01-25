'''
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

ALGO:
---------------
1. If you take one 3 you might as well take them all, you have already deleted all 2s and 4s anywas
2. For each new number, for example 3s, if we take them, we can't take 2s so our number will be the max we can take if we take 3s and 1s plus anything below
3. Our result is the maximum we can get from any number.

Ex.
2,2,3,3,3,4

DP[0] == 0
DP[2] == 2 * 2 = 4 + max(DP)
DP[3] == 3 * 3 = 9 + max(DP except for last) = 9 -- can't take 2s
DP[4] == 4 * 1 = 4 + max(DP except for last) = 8 -- can't take 3s

Best DP is 9
To optimize memory we just need to keep track of two values - max if we took last one
and max if we didn't
'''
from typing import List
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0, 0]
        counts = Counter(nums)
        numbers = sorted(counts.keys())

        prev = 0
        for num in numbers:
            if num - 1 == prev:
                dp.append(counts[num] * num + max(dp[:-1]))
            else:
                dp.append(counts[num] * num + max(dp))
            prev = num

        return max(dp)


solution = Solution()
assert solution.deleteAndEarn([1,1,1,2,4,5,5,5,6]) == 18
assert solution.deleteAndEarn([3, 4, 2]) == 6
assert solution.deleteAndEarn([2, 2, 3, 3, 3, 4]) == 9
