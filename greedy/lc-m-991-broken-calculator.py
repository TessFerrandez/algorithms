from collections import deque


class Solution:
    # memory limit exceeded
    def brokenCalc1(self, startValue: int, target: int) -> int:
        visited = set()
        todo = deque([(0, startValue)])

        while todo:
            steps, start = todo.popleft()
            if start == target:
                return steps

            visited.add(start)

            if start - 1 > 0 and (start - 1) not in visited:
                todo.append((steps + 1, start - 1))
            if start * 2 not in visited:
                todo.append((steps + 1, start * 2))

    # greedy - working backwards
    def brokenCalc(self, startValue: int, target: int) -> int:
        # if target is even 1 div + 1 add is same as 2 add + 1 div
        # if target is odd 1 add + 1 div + 1 add = 3 add + 1 div
        operations = 0

        while target > startValue:
            operations += 1
            if target % 2:
                target += 1
            else:
                target //= 2

        return operations + startValue - target


solution = Solution()
assert solution.brokenCalc(2, 3) == 2
assert solution.brokenCalc(5, 8) == 2
assert solution.brokenCalc(3, 10) == 3
