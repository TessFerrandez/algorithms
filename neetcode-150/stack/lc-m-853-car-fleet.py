from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort cars by start point
        cars = sorted(zip(position, speed))

        # calculate their time to target position
        time_to_pos = [float(target - pos) / spd for pos, spd in cars]

        fleets = current_head = 0
        for time in time_to_pos[::-1]:
            if time > current_head:
                # slower car behind => new fleet
                fleets += 1
                current_head = time

        return fleets


solution = Solution()
assert solution.carFleet(12, [10,8,0,5,3], [2, 4, 1, 1, 3]) == 3
assert solution.carFleet(10, [3], [3]) == 1
assert solution.carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
