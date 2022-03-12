'''
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
'''
from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_ends = set(deadends)

        def get_neighbors(state):
            neighbors = []
            for i in range(4):
                up = str((int(state[i]) + 1) % 10)
                neighbor = state[:i] + up + state[i + 1:]
                if neighbor not in dead_ends:
                    neighbors.append(neighbor)
                down = str((int(state[i]) - 1) % 10)
                neighbor = state[:i] + down + state[i + 1:]
                if neighbor not in dead_ends:
                    neighbors.append(neighbor)
            return neighbors

        if '0000' in dead_ends:
            return -1

        todo = deque([(0, '0000')])
        visited = set()

        while todo:
            steps, state = todo.popleft()

            if state in visited:
                continue

            if state == target:
                return steps

            visited.add(state)

            for neighbor in get_neighbors(state):
                todo.append((steps + 1, neighbor))

        return -1


solution = Solution()
assert solution.openLock(['0000'], '8888') == -1
assert solution.openLock(["0201","0101","0102","1212","2002"], '0202') == 6
assert solution.openLock(['8888'], '0009') == 1
assert solution.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], '8888') == -1
