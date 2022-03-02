'''
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
'''
from typing import List


class Solution:
    def summaryRanges1(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        low = -float('inf')
        high = float('inf')

        ranges = []
        for i, num in enumerate(nums):
            if num != high + 1:
                if i != 0:
                    if high == low:
                        ranges.append(str(low))
                    else:
                        ranges.append(f"{low}->{high}")
                low = num
                high = num
            else:
                high = num

        if high == low:
            ranges.append(str(low))
        else:
            ranges.append(f"{low}->{high}")

        return ranges

    def summaryRanges2(self, nums: List[int]) -> List[str]:
        ranges, current_range = [], []
        for num in nums:
            if num - 1 not in current_range:
                current_range = []
                ranges.append(current_range)

            current_range[1:] = [num]

        return ['->'.join(map(str, range)) for range in ranges]

    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []

        for num in nums:
            if not ranges or ranges[-1][-1] < num - 1:
                ranges.append([])
            ranges[-1][1:] = [num]

        return ['->'.join(map(str, range)) for range in ranges]


solution = Solution()
assert solution.summaryRanges([0]) == ["0"]
assert solution.summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
assert solution.summaryRanges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
