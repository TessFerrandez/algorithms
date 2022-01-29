'''
You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

-------------------
We can divide this up into START_GAIN (values[i] + i) and END_GAIN (values[j] - j)

Ex  [8, 1, 5, 2, 6]

I               0   1   2   3   4
START           8   2   7   5   10
END             8   0   3  -1   2
MaxEnd          8   3   3   2   2
Start + MaxEnd  11  5   9   7

8,1     9-1 = 8
8,5     13-2 = 11 MAX(0)
8,2     10-3 = 7
8,6     14-4 = 10
1,5     6-1 = 5 MAX(1)
1,2     3-2 = 1
1,6     7-3 = 4
5,2     7-1 = 6
5,6     11-2 = 9 MAX(2)
2,6     8-1 = 7 MAX(3)
'''
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_result = -(10 ** 9)
        max_end = values[-1] - (len(values) - 1)

        for i in range(len(values) - 2, -1, -1):
            max_result = max(max_result, i + values[i] + max_end)
            max_end = max(max_end, values[i] - i)

        return max_result


solution = Solution()
assert solution.maxScoreSightseeingPair([8, 1, 5, 2, 6]) == 11
assert solution.maxScoreSightseeingPair([1, 2]) == 2
