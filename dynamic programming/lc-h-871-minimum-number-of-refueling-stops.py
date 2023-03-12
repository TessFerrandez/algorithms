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

    def minRefuelStops2(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
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

    # this has terrible naming - for a demo about bad naming
    def min_refuel_stops(self, tgt: int, sf: int, A: List[List[int]]) -> int:
        dp = [sf] + [0] * len(A)
        for i, (l, c) in enumerate(A):
            for t in range(i, -1, -1):
                if dp[t] >= l:
                    dp[t + 1] = max(dp[t + 1], dp[t] + c)
        for i, d in enumerate(dp):
            if d >= tgt:
                return i
        return -1

    def min_refuel_stops2(self, target: int, start_fuel: int, stations: List[List[int]]) -> int:
        farthest_location = [start_fuel] + [0] * len(stations)

        for station_idx, (location, capacity) in enumerate(stations):
            for station_idx in range(station_idx, -1, -1):
                if farthest_location[station_idx] >= location:
                    farthest_location[station_idx + 1] = max(farthest_location[station_idx + 1], farthest_location[station_idx] + capacity)

        for stops, distance in enumerate(farthest_location):
            if distance >= target:
                return stops

        return -1

    def min_refuel_stops4(self, target: int, start_fuel: int, stations: List[List[int]]) -> int:
        def get_max_distance_by_number_of_stops(start_fuel, stations):
            max_distance_by_stops = [start_fuel] + [0] * len(stations)

            for station_idx, (location, capacity) in enumerate(stations):
                for station_idx in range(station_idx, -1, -1):
                    if max_distance_by_stops[station_idx] >= location:
                        max_distance_by_stops[station_idx + 1] = max(max_distance_by_stops[station_idx + 1], max_distance_by_stops[station_idx] + capacity)

            return max_distance_by_stops

        def get_minimum_stops_needed(max_distance_by_stops):
            for stops, distance in enumerate(max_distance_by_stops):
                if distance >= target:
                    return stops

            return -1

        max_distance_by_stops = get_max_distance_by_number_of_stops(start_fuel, stations)
        return get_minimum_stops_needed(max_distance_by_stops)


solution = Solution()
assert solution.min_refuel_stops(100, 10, [[10,60], [20, 30], [30, 30], [60, 40]]) == 2
assert solution.min_refuel_stops(1, 1, []) == 0
assert solution.min_refuel_stops(100, 1, [[10, 100]]) == -1
