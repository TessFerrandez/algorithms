from typing import List


MOD = 10 ** 9 + 7


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        # ways to reach n points
        ways_to_reach = [1] + [0] * target

        for count, marks in types:
            for points in range(target, -1, -1):
                for k in range(1, min(count, points // marks) + 1):
                    ways_to_reach[points] = (ways_to_reach[points] + ways_to_reach[points - marks * k]) % MOD

        return ways_to_reach[-1]


solution = Solution()
assert solution.waysToReachTarget(6, [[6,1],[3,2],[2,3]]) == 7
assert solution.waysToReachTarget(5, [[50,1],[50,2],[50,5]]) == 4
assert solution.waysToReachTarget(18, [[6,1],[3,2],[2,3]]) == 1
