from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
    def minRefuelStops1(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel] + [0] * len(stations)

        for i, (location, capacity) in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t] >= location:
                    dp[t + 1] = max(dp[t + 1], dp[t] + capacity)

        for i, d in enumerate(dp):
            if d >= target:
                return i

        return -1

    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []
        stations.append((target, inf))
        tank = startFuel

        answer = prev = 0
        for location, capacity in stations:
            tank -= location - prev
            while pq and tank < 0:  # must refuel in the past
                tank += -heappop(pq)
                answer += 1
            if tank < 0:
                return -1
            heappush(pq, -capacity)
            prev = location

        return answer


solution = Solution()
assert solution.minRefuelStops(1, 1, []) == 0
assert solution.minRefuelStops(100, 1, [[10, 100]]) == -1
assert solution.minRefuelStops(100, 10, [[10,60], [20, 30], [30, 30], [60, 40]]) == 2
