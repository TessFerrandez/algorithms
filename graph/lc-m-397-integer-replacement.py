'''
Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.
'''
from collections import deque


class Solution:
    def integerReplacement(self, n: int) -> int:
        def get_neighbors(current):
            if current % 2 == 0:
                return [current // 2]
            else:
                return [current + 1, current - 1]

        todo = deque([(n, 0)])
        visited = set([n])

        if n == 1:
            return 0

        while todo:
            current, steps = todo.popleft()

            for neighbor in get_neighbors(current):
                if neighbor == 1:
                    return steps + 1

                if neighbor not in visited:
                    visited.add(neighbor)
                    todo.append((neighbor, steps + 1))

        return -1


solution = Solution()
assert solution.integerReplacement(8) == 3
assert solution.integerReplacement(7) == 4
assert solution.integerReplacement(4) == 2
