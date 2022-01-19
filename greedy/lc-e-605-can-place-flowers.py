'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Algorithm
-----------------
Ex 0-0-1-0-1
Extend the flowerbed to (1)-(0)-0-0-1-0-1-(0)-(1) to account for the edges
Check the gaps,
If the gap is 3 or more, you can place one on prev + 2 prev + 2 now becomes the new previous.
Finish when you planted all flowers or reached the end of the flowerbed
'''
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        flowers = [i for i, pot in enumerate(flowerbed) if pot == 1] + [len(flowerbed) + 1]
        prev = -2
        i = 0

        while n > 0 and i < len(flowers):
            if flowers[i] - prev > 3:
                prev += 2
                n -= 1
            else:
                prev = flowers[i]
                i += 1

        return n == 0


solution = Solution()
assert solution.canPlaceFlowers([0, 0, 1, 0, 1], 1) == True
assert solution.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2) == False
assert solution.canPlaceFlowers([1, 0, 0, 0, 1], 1) == True
assert solution.canPlaceFlowers([1, 0, 0, 0, 1], 2) == False
