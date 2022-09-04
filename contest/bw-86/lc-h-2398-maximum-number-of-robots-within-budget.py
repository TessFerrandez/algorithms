from collections import defaultdict, deque
from heapq import heappop, heappush
from typing import List
from sortedcontainers import SortedList


class Solution:
    # mine - wrong solution
    def maximumRobots1(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        valid_arrays = defaultdict(list)

        n = len(chargeTimes)
        left = 0

        curr_sum = 0
        curr_len = 0
        for right in range(n):
            curr_sum += runningCosts[right]
            curr_len += 1

            while curr_sum * curr_len > budget:
                curr_sum -= runningCosts[left]
                curr_len -= 1
                left += 1

            valid_arrays[curr_len].append((left, right, curr_sum * curr_len))

        # print(valid_arrays)

        for arr_len in list(valid_arrays.keys())[::-1]:
            if arr_len == 0:
                return 0
            for arr in valid_arrays[arr_len]:
                if max(chargeTimes[arr[0]: arr[1] + 1]) + arr[2] <= budget:
                    return arr_len

        return 0

    # solution adapted from other player
    def maximumRobots2(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        def get_max_in_range(max_heap, left):
            # remove any out of range
            while max_heap and max_heap[0][1] <= left:
                heappop(max_heap)
            return -max_heap[0][0] if max_heap else 0

        max_robots, running_sum, left, max_heap = 0, 0, -1, []

        for right in range(len(runningCosts)):
            # try expanding
            running_sum += runningCosts[right]
            heappush(max_heap, (-chargeTimes[right], right))

            # shrink until we are within budget
            while running_sum * (right - left) + get_max_in_range(max_heap, left) > budget:
                left += 1
                running_sum -= runningCosts[left]

            # record the maximum number of robots
            max_robots = max(max_robots, right - left)

        return max_robots

    # same with sorted list instead of heap
    def maximumRobots3(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        current_cost = left = 0
        n = len(chargeTimes)
        max_times = SortedList()

        for right in range(n):
            current_cost += runningCosts[right]
            max_times.add(chargeTimes[right])

            if max_times[-1] + (right - left + 1) * current_cost > budget:
                max_times.remove(chargeTimes[left])
                current_cost -= runningCosts[left]
                left += 1

        return n - left

    # same with deque instead of heap
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        current_cost = left = 0
        n = len(chargeTimes)
        d = deque()

        for right in range(n):
            current_cost += runningCosts[right]
            while d and chargeTimes[d[-1]] <= chargeTimes[right]:
                d.pop()

            d.append(right)

            if chargeTimes[d[0]] + (right - left + 1) * current_cost > budget:
                if d[0] == left:
                    d.popleft()
                current_cost -= runningCosts[left]
                left += 1

        return n - left


solution = Solution()
assert solution.maximumRobots([956,379,920,977,331,569,212,590,569,940,106,588,284,12,912,950,525,535,491,928,335,840,596,378,458,226,817,912,90,444,93,182,395,241,184,817,998,690,551,806,803,656,490,251,496,311,181,221,982,148,411,384,710,330,345,728,17,74,377,456,439,58,788,950,70,263,473,932,649,354,763,848,212,363,491,108,222,544,238,890,811,428,963,476,984,951,29,408,48,313,718,361,673,760,206,991,360,463,114,703,401,893,304,49,689,915,917,43,999,361,204,56,306,321,495,254,277,174,539,621,803,14,759,437,405,101,383,617,945,739,674,88],[2,10,6,3,5,3,2,3,10,6,8,2,4,5,6,2,4,2,6,3,1,5,4,9,9,5,2,7,6,10,8,7,5,1,7,9,8,7,4,3,3,9,8,5,6,3,1,7,10,7,10,10,7,4,6,10,6,2,2,10,2,9,2,2,5,7,9,5,4,7,6,7,3,7,7,1,2,6,10,2,8,8,10,1,4,1,4,4,5,4,5,2,8,8,9,2,3,1,6,10,5,2,1,6,9,4,7,6,7,1,2,1,2,6,9,3,9,6,4,10,6,4,10,5,8,9,6,10,4,4,5,2],25205) == 68
assert solution.maximumRobots([52,30,69,7,60,11,34,34,12,77,18,1,2,53,40,54,14,93,12,83,74,78,74,45,49,55,33,88,36,30,64,11,91,80,97,55,16,70,14,75,19,11,6,86,59,58,46,72,18,90,7,25,56,42,78,12,63,10,40,40,70,45,9,66,24,16,69,63,94,84,43,36,40,59,26,94], [39,23,11,18,80,82,62,69,67,14,53,37,89,82,86,29,13,71,6,93,73,100,82,46,6,69,81,68,73,86,47,98,61,86,53,55,9,51,26,29,76,14,61,2,83,29,10,87,64,97,38,66,100,90,45,42,55,98,46,18,23,18,99,12,50,32,61,89,35,83,99,2,22,82,3,61], 10) == 0
assert solution.maximumRobots([3,6,1,3,4], [2,1,3,4,5], 25) == 3
assert solution.maximumRobots([11,12,19], [10,8,7], 19) == 0
