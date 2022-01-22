'''

User Accepted:3213
User Tried:5309
Total Accepted:3320
Total Submissions:13663
Difficulty:Medium
You are given a 0-indexed array of n integers differences, which describes the differences between each pair of consecutive integers of a hidden sequence of length (n + 1). More formally, call the hidden sequence hidden, then we have that differences[i] = hidden[i + 1] - hidden[i].

You are further given two integers lower and upper that describe the inclusive range of values [lower, upper] that the hidden sequence can contain.

For example, given differences = [1, -3, 4], lower = 1, upper = 6, the hidden sequence is a sequence of length 4 whose elements are in between 1 and 6 (inclusive).
[3, 4, 1, 5] and [4, 5, 2, 6] are possible hidden sequences.
[5, 6, 3, 7] is not possible since it contains an element greater than 6.
[1, 2, 3, 4] is not possible since the differences are not correct.
Return the number of possible hidden sequences there are. If there are no possible sequences, return 0.
'''
from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        curr_low, curr_up = lower, upper

        for diff in differences:
            if diff >= 0:
                curr_low += diff
                if curr_low > upper:
                    return 0
                curr_up = min(upper, curr_up + diff )
            else:
                curr_low = max(lower, curr_low + diff)
                curr_up += diff
                if curr_up < lower:
                    return 0

        return curr_up - curr_low + 1


solution = Solution()
assert solution.numberOfArrays([4, -7, 2], 3, 6) == 0
assert solution.numberOfArrays([1, -3, 4], 1, 6) == 2
assert solution.numberOfArrays([3, -4, 5, 1, -2], -4, 5) == 4
