class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        total = ''
        for num in range(1, n + 1):
            total += bin(num)[2:]

        return int(total, 2) % MOD


solution = Solution()
assert solution.concatenatedBinary(1) == 1
assert solution.concatenatedBinary(3) == 27
assert solution.concatenatedBinary(12) == 505379714
