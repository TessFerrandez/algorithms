'''
You have some apples, where arr[i] is the weight of the i-th apple.  You also have a basket that can carry up to 5000 units of weight.

Return the maximum number of apples you can put in the basket.
'''
from typing import List


class Solution:
    def max_num_apples(self, apples: List[int]) -> int:
        n = len(apples)
        weight = sum(apples)

        if weight <= 5000:
            return n

        apples.sort()

        while weight >= 5000:
            weight -= apples.pop()
            n -= 1

        return n


solution = Solution()
assert solution.max_num_apples([100, 200, 150, 1000]) == 4
assert solution.max_num_apples([900, 950, 800, 1000, 700, 800]) == 5
assert solution.max_num_apples([200, 200, 1000, 300, 1000, 800, 900, 1000, 1000]) == 7
