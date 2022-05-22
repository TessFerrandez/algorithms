from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = 1 + candies[i - 1]

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], 1 + candies[i + 1])

        return sum(candies)


solution = Solution()
assert solution.candy([1, 0, 2]) == 5
assert solution.candy([1, 2, 2]) == 4
assert solution.candy([2, 1, 0, 2]) == 8
