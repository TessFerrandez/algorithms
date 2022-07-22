class Solution:
    def minOperations(self, n: int) -> int:
        total = 0

        if n % 2 == 0:
            for i in range(n // 2):
                total += (2 * i) + 1
        else:
            for i in range(n // 2):
                total += (2 * (i + 1))

        return total


solution = Solution()
assert solution.minOperations(1) == 0
assert solution.minOperations(2) == 1
assert solution.minOperations(3) == 2
assert solution.minOperations(4) == 4
assert solution.minOperations(5) == 6
assert solution.minOperations(6) == 9
