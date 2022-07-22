class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        pens = total // cost1

        ways = 0
        for n_pens in range(pens + 1):
            ways += (total - (n_pens * cost1)) // cost2 + 1
        return ways


solution = Solution()
assert solution.waysToBuyPensPencils(20, 10, 5) == 9
assert solution.waysToBuyPensPencils(5, 10, 10) == 1
