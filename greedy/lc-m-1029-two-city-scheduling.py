'''
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.
'''
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs.sort(key=lambda x: x[0] - x[1])

        total_cost = sum(cost[0] for cost in costs[:n])
        total_cost += sum(cost[1] for cost in costs[n:])
        return total_cost


solution = Solution()
assert solution.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]) == 1859
assert solution.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]) == 110
assert solution.twoCitySchedCost([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]) == 3086
