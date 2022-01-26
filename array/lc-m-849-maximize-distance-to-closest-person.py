'''
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to the closest person.
'''
from typing import List


class Solution:
    # my solution
    def maxDistToClosest1(self, seats: List[int]) -> int:
        n = len(seats)
        max_dist = [0 for _ in range(n)]

        # from start
        last_full = -1
        for i, seat in enumerate(seats):
            if seat == 0:
                if last_full == -1:
                    max_dist[i] = 10 ** 6
                else:
                    max_dist[i] = i - last_full
            else:
                last_full = i

        # from end
        last_full = -1
        for i in range(n - 1, -1, -1):
            if seats[i] == 0:
                if last_full != -1:
                    max_dist[i] = min(max_dist[i], last_full - i)
            else:
                last_full = i

        return max(max_dist)

    # two pointer from solution doc
    def maxDistToClosest2(self, seats):
        people = (i for i, seat in enumerate(seats) if seat)
        prev, future = None, next(people)

        ans = 0
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)

                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                ans = max(ans, min(left, right))

        return ans

    # based on groupings of 0s - also based on solution doc
    def maxDistToClosest(self, seats):
        # for groups at the end, sit at the farthest seat
        max_dist = seats.index(1)
        seats.reverse()
        max_dist = max(max_dist, seats.index(1))

        # count the largest group of consecutive 0s
        # the max dist is middle of that group
        current_group = 0
        for seat in seats:
            if seat:
                max_dist = max(max_dist, (current_group + 1) // 2)
                current_group = 0
            else:
                current_group += 1

        return max_dist


solution = Solution()
assert solution.maxDistToClosest([0, 1]) == 1
assert solution.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]) == 2
assert solution.maxDistToClosest([1, 0, 0, 0]) == 3
