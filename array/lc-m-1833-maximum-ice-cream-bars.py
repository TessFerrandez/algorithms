from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        icecreams = 0
        while icecreams < len(costs) and costs[icecreams] <= coins:
            coins -= costs[icecreams]
            icecreams += 1

        return icecreams


solution = Solution()
assert solution.maxIceCream([1, 3, 2, 4, 1], 7) == 4
assert solution.maxIceCream([10, 6, 8, 7, 7, 8], 5) == 0
assert solution.maxIceCream([1, 6, 3, 1, 2, 5], 20) == 6
