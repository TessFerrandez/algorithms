# array, greedy
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        # forward pass
        for i, (prev, next) in enumerate(zip(ratings, ratings[1:])):
            if next > prev:
                candies[i + 1] = candies[i] + 1

        # backward pass
        for i, (prev, next) in enumerate(zip(ratings[::-1], ratings[-2::-1])):
            if next > prev:
                candies[-2 - i] = max(candies[-2 - i], candies[-1 - i] + 1)

        return sum(candies)


solution = Solution()
assert solution.candy([1, 0, 2]) == 5
assert solution.candy([1, 2, 2]) == 4
