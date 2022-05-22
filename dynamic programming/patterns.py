'''
1. Minimum/Maximum path to reach target
2. Distinct ways
3. Merging intervals
4. DP on strings
5. Decision Making
'''
# PROBLEM: Min/Max path to reach target
# APPROACH: Chose min path among all possible paths before current state
# then add current cost
from functools import cache


# top-down -- minimum cost to climb stairs, climb 1-2 steps at a time
def minCostClimbingStairs1(stairs):
    @cache
    def min_cost(n):
        if n <= 1:
            return 0
        return min(min_cost(n - 1) + stairs[n - 1], min_cost(n - 2) + stairs[n - 2])
    return min_cost(len(stairs))


# bottom up
def minCostClimbingStairs2(stairs):
    costs = [0, 0]

    for i in range(2, len(stairs) + 1):
        costs.append(min(costs[i - 1] + stairs[i - 1], costs[i - 2] + stairs[i - 2]))

    return costs[len(stairs)]


# bottom up - save space
def minCostClimbingStairs(stairs):
    c1, c2 = 0, 0

    for i in range(2, len(stairs) + 1):
        cost = min(c1 + stairs[i - 2], c2 + stairs[i - 1])
        c1, c2 = c2, cost

    return c2


assert minCostClimbingStairs([10, 15, 20]) == 15
assert minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6


# longest-increasing-subsequence
def lengthOfLIS(nums):
    n = len(nums)
    longest = [1] * n

    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                longest[j] = max(longest[j], 1 + longest[i])

    return max(longest)


assert lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
assert lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
assert lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
