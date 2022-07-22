from cmath import inf
from typing import List
from decimal import getcontext, Decimal


class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        getcontext().prec = 50
        stockPrices.sort()
        if len(stockPrices) == 1:
            return 0
        if len(stockPrices) == 2:
            return 1

        dy = stockPrices[1][1] - stockPrices[0][1]
        dx = stockPrices[1][0] - stockPrices[0][0]
        if dx == 0:
            k = inf
        else:
            k = Decimal(dy) / Decimal(dx)

        count = 1

        xp, yp = stockPrices[1]
        for x, y in stockPrices[2:]:
            dy, dx = y - yp, x - xp
            if dx == 0:
                if k != inf:
                    count += 1
                    k = inf
            elif Decimal(dy) / Decimal(dx) != k:
                k = Decimal(dy) / Decimal(dx)
                count += 1
            xp, yp = x, y
        return count


solution = Solution()
assert solution.minimumLines([[1,1],[500000000,499999999],[1000000000,999999998]]) == 2
assert solution.minimumLines([[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]) == 3
assert solution.minimumLines([[3,4],[1,2],[7,8],[2,3]]) == 1
assert solution.minimumLines([[72,98],[62,27],[32,7],[71,4],[25,19],[91,30],[52,73],[10,9],[99,71],[47,22],[19,30],[80,63],[18,15],[48,17],[77,16],[46,27],[66,87],[55,84],[65,38],[30,9],[50,42],[100,60],[75,73],[98,53],[22,80],[41,61],[37,47],[95,8],[51,81],[78,79],[57,95]]) == 29
