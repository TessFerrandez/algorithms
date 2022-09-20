class Solution:
    def lastRemaining1(self, n: int) -> int:
        '''
        core idea mid_left(1..n) + mid_right(1..n) = 1 + n
        '''
        return 1 if n == 1 else 2 * (1 + n // 2 - self.lastRemaining(n // 2))

    def lastRemaining2(self, n: int) -> int:
        head, step = 1, 1
        right = True

        while n > 1:
            if right:
                head += step
            else:
                head += 0 if n % 2 == 0 else step
            step *= 2
            n //= 2
            right = not right

        return head

    def lastRemaining(self, n: int) -> int:
        def right_to_left(n):
            if n == 1:
                return 1

            if n % 2 == 0:
                # if the length is even, we will get only odd numbers
                # [1, 2, 3, 4] => [1, 3] = 2 * [1, 2] - 1
                return 2 * left_to_right(n // 2) - 1
            else:
                # if the length is odd, we will get only even numbers
                # [1, 2, 3, 4, 5] => [2, 4] = 2 * [1, 2]
                return 2 * left_to_right(n // 2)

        def left_to_right(n):
            if n == 1:
                return 1

            # length of array doesn't matter from left to right
            # [1, 2, 3, 4] => [2, 4] = 2 * [1, 2]
            # [1, 2, 3, 4, 5] => [2, 4] = 2 * [1, 2]
            return 2 * right_to_left(n // 2)

        return left_to_right(n)


solution = Solution()
assert solution.lastRemaining(9) == 6
assert solution.lastRemaining(1) == 1
