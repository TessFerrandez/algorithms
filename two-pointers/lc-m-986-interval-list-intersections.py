'''
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

Agorithm:
---------------------
Ex: [[0,2],[5,10]] and [[1,5],[8,12]]

        0   1   2   3   4   5   6   7   8   9   10  11  12
First   X   X   X           X   X   X   X   X   X
Second      X   X   X   X   X           X   X   X   X   X

1. Compare 0,2 with 1,5     - Overlap = Max(0, 1), Min(2, 5) == [1,2]
    Since end of 1st is lower than end of 2nd, move 1st forward
2. Compare 5,6 with 1,5     - Overlap [5,5]
    Since end of 1st is higher than end of 2nd, move 2nd forward
3. Compare 5,6 with 8,12    - Overlap [8,10]
    Since end of 1st is lower than end of 2nd, move 1st forward
4. Done
'''
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i_first, i_second = 0, 0
        n_first, n_second = len(firstList), len(secondList)

        result = []

        while i_first < n_first and i_second < n_second:
            low = max(firstList[i_first][0], secondList[i_second][0])
            high = min(firstList[i_first][1], secondList[i_second][1])

            if high >= low:
                result.append([low, high])

            if firstList[i_first][1] >= secondList[i_second][1]:
                i_second += 1
            else:
                i_first += 1

        return result


solution = Solution()
assert solution.intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]) == [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
assert solution.intervalIntersection([[1,3],[5,9]], []) == []
