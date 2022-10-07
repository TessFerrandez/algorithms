from collections import deque


class Solution:
    # BFS solution O(presses)
    def flipLights1(self, n: int, presses: int) -> int:
        def flip_all(state, n):
            x = (1 << n) - 1
            return state ^ x

        def flip_even(state, n):
            for i in range(0, n, 2):
                state ^= 1 << i
            return state

        def flip_odd(state, n):
            for i in range(1, n, 2):
                state ^= 1 << i
            return state

        def flip3k1(state, n):
            for i in range(0, n, 3):
                state ^= 1 << i
            return state

        n = n if n <= 6 else (n % 6 + 6)

        visited = set()
        queue = deque()

        initial = (1 << n) - 1
        queue.append(initial)

        for _ in range(presses):
            size = len(queue)
            visited.clear()

            for _ in range(size):
                state = queue.popleft()
                neighbors = flip_all(state, n), flip_even(state, n), flip_odd(state, n), flip3k1(state, n)
                for next_state in neighbors:
                    if next_state not in visited:
                        queue.append(next_state)
                        visited.add(next_state)

        return len(queue)

    # math O(1)
    def flipLights(self, n: int, presses: int) -> int:
        '''
        There are only so many states (0*, 1*, 01*, 10*, 011*, 100*, 001110*, 110001*) and then you flip between them
        '''
        if presses == 0:
            return 1
        if n == 1:
            return 2
        elif n == 2:
            if presses == 1:
                return 3
            else:
                return 4
        else:
            if presses == 1:
                return 4
            elif presses == 2:
                return 7
            else:
                return 8


solution = Solution()
assert solution.flipLights(1, 1) == 2
assert solution.flipLights(2, 1) == 3
assert solution.flipLights(3, 1) == 4
