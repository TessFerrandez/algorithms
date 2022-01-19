'''
You have n computers. You are given the integer n and a 0-indexed integer array batteries where the ith battery can run a computer for batteries[i] minutes. You are interested in running all n computers simultaneously using the given batteries.

Initially, you can insert at most one battery into each computer. After that and at any integer time moment, you can remove a battery from a computer and insert another battery any number of times. The inserted battery can be a totally new battery or a battery from another computer. You may assume that the removing and inserting processes take no time.

Note that the batteries cannot be recharged.

Return the maximum number of minutes you can run all the n computers simultaneously.

Algorithm:
-------------------
Pick up the best n batteries, and think of the rest as a resevoir of extra charge

1. give all the extra charge to the lowest battery, and check if it can last as much as the 2nd lowest
    else return (lowest + extra)
2. give extra resevoir to the lowest and 2nd lowest and check if it can last as much as 3rd best,
    else return (lowest + 2nd lowest + extra) // 2
3. continue like this with all batteries
4. if we never stopped, return (sum(batteries) + extra) // n
'''
from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        extra = sum(batteries[: -n])
        batteries = batteries[-n:]

        prefix = 0
        for i, charge in enumerate(batteries):
            prefix += charge
            if i + 1 < len(batteries) and batteries[i + 1] * (i + 1) - prefix > extra:
                return (prefix + extra) // (i + 1)

        return (prefix + extra) // n


solution = Solution()
assert solution.maxRunTime(2, [3, 3, 3]) == 4
assert solution.maxRunTime(2, [1, 1, 1, 1]) == 2
