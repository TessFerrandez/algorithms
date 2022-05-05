from functools import cache
from typing import List


class Solution:
    # top down (template)
    def mincostTickets1(self, days: List[int], costs: List[int]) -> int:
        dayset = set(days)
        durations = [1, 7, 30]

        @cache
        def get_min_cost(day):
            if day > 365:
                return 0
            elif day in dayset:
                return min(get_min_cost(day + ticket_days) + ticket_cost for ticket_cost, ticket_days in zip(costs, durations))
            else:
                return get_min_cost(day + 1)

        return get_min_cost(1)

    # top down (template)
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        durations = [1, 7, 30]

        @cache
        def get_min_cost(day_i):
            if day_i >= n:
                return 0

            result = float('inf')
            day2_i = day_i
            for ticket_cost, ticket_duration in zip(costs, durations):
                while day2_i < n and days[day2_i] < days[day_i] + ticket_duration:
                    day2_i += 1
                result = min(result, get_min_cost(day2_i) + ticket_cost)
            return result

        return get_min_cost(0)


solution = Solution()
assert solution.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]) == 11
assert solution.mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2, 7, 15]) == 17
