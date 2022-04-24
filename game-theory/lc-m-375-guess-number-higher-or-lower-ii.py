class Solution:
    # bottom up dynamic programming
    def getMoneyAmount(self, n: int) -> int:
        need = [[0] * (n + 1) for _ in range(n + 1)]

        for low in range(n, 0, -1):
            for high in range(low + 1, n + 1):
                need[low][high] = min(x + max(need[low][x - 1], need[x + 1][high]) for x in range(low, high))

        return need[1][n]


solution = Solution()
assert solution.getMoneyAmount(10) == 16
assert solution.getMoneyAmount(1) == 0
assert solution.getMoneyAmount(2) == 1
