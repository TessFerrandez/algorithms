'''
A certain bug's home is on the x-axis at position x. Help them get there from position 0.

The bug jumps according to the following rules:

It can jump exactly a positions forward (to the right).
It can jump exactly b positions backward (to the left).
It cannot jump backward twice in a row.
It cannot jump to any forbidden positions.
The bug may jump forward beyond its home, but it cannot jump to positions numbered with negative integers.

Given an array of integers forbidden, where forbidden[i] means that the bug cannot jump to the position forbidden[i], and integers a, b, and x, return the minimum number of jumps needed for the bug to reach its home. If there is no possible sequence of jumps that lands the bug on position x, return -1.
'''
from collections import deque
from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        max_n = 8000
        forbidden = set(forbidden)

        visited = set([(False, 0)])
        todo = deque([(0, False, 0)])

        while todo:
            steps, back, location = todo.popleft()
            if location == x:
                return steps
            if not back and location - b >= 0 and (True, location - b) not in visited and (location - b) not in forbidden:
                todo.append((steps + 1, True, location - b))
                visited.add((True, location - b))
            if location + a <= max_n and (False, location + a) not in visited and (location + a) not in forbidden:
                todo.append((steps + 1, False, location + a))
                visited.add((False, location + a))

        return -1


solution = Solution()
assert solution.minimumJumps([1998], 1999, 2000, 2000) == 3998
assert solution.minimumJumps([162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98], 29, 98, 80) == 121
assert solution.minimumJumps([1,6,2,14,5,17,4], 16, 9, 7) == 2
assert solution.minimumJumps([14,4,18,1,15], 3, 15, 9) == 3
assert solution.minimumJumps([8,3,16,6,12,20], 15, 13, 11) == -1
