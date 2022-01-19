'''
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
'''
from typing import List
from collections import Counter


def all_divisible(nums, divisor):
    for num in nums:
        if num % divisor != 0:
            return False
    return True


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 0:
            return False

        counts = Counter(deck)
        min_size = min(counts.values())

        for i in range(2, min_size + 1):
            if all_divisible(counts.values(), i):
                return True

        return False


solution = Solution()
assert solution.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]) == True
assert solution.hasGroupsSizeX([1, 1, 1, 2, 2, 3, 3]) == False
assert solution.hasGroupsSizeX([1, 1, 1, 1, 2, 2, 2, 2, 2, 2]) == True
