# array, greedy
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        current_surplus = 0
        total_surplus = 0
        start = 0

        for station_number, (station_gas, station_cost) in enumerate(zip(gas, cost)):
            current_surplus += station_gas - station_cost
            total_surplus += station_gas - station_cost

            if current_surplus < 0:
                current_surplus = 0
                start = station_number + 1

        return -1 if total_surplus < 0 else start


solution = Solution()
assert solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
assert solution.canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1
