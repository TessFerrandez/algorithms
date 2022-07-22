'''
You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.
'''
from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        if len(time) == 1:
            return totalTrips * time[0]

        low, high = 0, min(time) * totalTrips

        while low < high:
            mid = (low + high) // 2
            result = 0

            for bus in time:
                result += mid // bus

            if result >= totalTrips:
                high = mid
            else:
                low = mid + 1

        return low


solution = Solution()
assert solution.minimumTime([9, 3, 10, 5], 2) == 5
assert solution.minimumTime([5, 10, 10], 9) == 25
assert solution.minimumTime([1, 2, 3], 5) == 3
assert solution.minimumTime([2], 1) == 2
