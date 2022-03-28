from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        cache = [[None for _ in range(k + 2)] for _ in range(len(piles) + 1)]

        def dp(i, k):
            if k == 0 or i == len(piles):
                return 0

            if cache[i][k]:
                return cache[i][k]

            result = dp(i + 1, k)
            current = 0

            for j in range(min(len(piles[i]), k)):
                current += piles[i][j]
                result = max(result, current + dp(i + 1, k - j - 1))

            cache[i][k] = result
            return result

        return dp(0, k)


solution = Solution()
print(solution.maxValueOfCoins([[1, 100, 3], [7, 8, 9]], 2))
print(solution.maxValueOfCoins([[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]], 7))
