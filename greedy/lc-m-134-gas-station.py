'''
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
'''
from typing import List


class Solution:
    # my solution
    def canCompleteCircuit1(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if n == 0:
            return -1

        surplus = [gas[i] - cost[i] for i in range(n)]

        # if we don't have more gas than total cost, we'll never make it
        if sum(surplus) < 0:
            return -1

        # sort stations based on how much of a surplus you'll have after the next
        sorted_stations = [i[0] for i in sorted(enumerate(surplus), key=lambda x: x[1])][::-1]

        # go through the stations
        for station in sorted_stations:
            next_station = (station + 1) % n
            current_gas = surplus[station]

            while next_station != station and current_gas >= 0:
                current_gas += surplus[next_station]
                next_station = (next_station + 1) % n

            if current_gas >= 0:
                return station

        return -1

    # highly optimized O(n) time O(1) space
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if the sum of the gas - sum of the cost we can never make it
        # no matter where we start
        if (sum(gas) - sum(cost)) < 0:
            return -1

        # if the result is more than 0 we can do it
        gas_tank, start_index = 0, 0

        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]

            if gas_tank < 0:
                # first station that clears it all the way to the end is a winner
                start_index = i + 1
                gas_tank = 0

        return start_index


solution = Solution()
assert solution.canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1
assert solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
