'''
Given n orders, each order consist in pickup and delivery services.

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i).

Since the answer may be too large, return it modulo 10^9 + 7.
'''
class Solution:
    def countOrders(self, n: int) -> int:
        slots = 2 * n
        total_ways = 1

        while slots > 0:
            total_ways *= (slots * (slots - 1)) // 2
            slots -= 2

        return total_ways


solution = Solution()
assert solution.countOrders(1) == 1
assert solution.countOrders(2) == 6
assert solution.countOrders(3) == 90
print(solution.countOrders(4))
