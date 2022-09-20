from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available = [room for room in range(n)]
        rooms_in_use = []       # (end_time, room_index)
        meeting_count = [0] * n

        def finish_any_meetings_that_will_be_over_before_next_start_time(start):
            while rooms_in_use and rooms_in_use[0][0] <= start:
                _, room = heappop(rooms_in_use)
                heappush(available, room)

        def start_meeting_now(end):
            room = heappop(available)
            heappush(rooms_in_use, [end, room])
            return room

        def schedule_meeting_later(start, end):
            finish_time, room = heappop(rooms_in_use)
            heappush(rooms_in_use, [finish_time + end - start, room])
            return room

        heapify(available)

        for start, end in sorted(meetings):
            finish_any_meetings_that_will_be_over_before_next_start_time(start)

            if available:
                room = start_meeting_now(end)
            else:
                room = schedule_meeting_later(start, end)

            meeting_count[room] += 1

        return meeting_count.index(max(meeting_count))


solution = Solution()
assert solution.mostBooked(2, [[0,10],[1,5],[2,7],[3,4]]) == 0
assert solution.mostBooked(3, [[1,20],[2,10],[3,5],[4,9],[6,8]]) == 1
assert solution.mostBooked(2, [[0,10],[1,2],[12,14],[13,15]]) == 0
