'''
You are given two jugs with capacities jug1Capacity and jug2Capacity liters. There is an infinite amount of water supply available. Determine whether it is possible to measure exactly targetCapacity liters using these two jugs.

If targetCapacity liters of water are measurable, you must have targetCapacity liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.
'''
from collections import deque


class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        todo = deque([(0, 0)])
        visited = set()

        while todo:
            jug1, jug2 = todo.popleft()

            if (jug1, jug2) in visited:
                continue

            visited.add((jug1, jug2))
            total = jug1 + jug2

            if total == targetCapacity:
                return True

            todo.append((jug1, jug2Capacity))
            todo.append((jug1Capacity, jug2))
            todo.append((0, jug2))
            todo.append((jug1, 0))

            if total > jug1Capacity:
                # pour jug2 into jug1
                todo.append((jug1Capacity, jug2 - (jug1Capacity - jug1)))

            if total <= jug1Capacity:
                # pour jug2 into jug1
                todo.append((total, 0))

            if total > jug2Capacity:
                # pour jug1 into jug2
                todo.append((jug1 - (jug2Capacity - jug2), jug2Capacity))

            if total <= jug2Capacity:
                # pour jug1 into jug2
                todo.append((0, total))

        return False


solution = Solution()
assert solution.canMeasureWater(3, 5, 4)
assert not solution.canMeasureWater(2, 6, 5)
assert solution.canMeasureWater(1, 2, 3)
