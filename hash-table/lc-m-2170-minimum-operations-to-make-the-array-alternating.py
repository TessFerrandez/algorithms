'''
You are given a 0-indexed array nums consisting of n positive integers.

The array nums is called alternating if:

nums[i - 2] == nums[i], where 2 <= i <= n - 1.
nums[i - 1] != nums[i], where 1 <= i <= n - 1.
In one operation, you can choose an index i and change nums[i] into any positive integer.

Return the minimum number of operations required to make the array alternating.
'''
from typing import List
from collections import Counter


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        first = second = n // 2
        if n % 2:
            first += 1

        count1 = Counter(nums[::2]).most_common()
        count2 = Counter(nums[1::2]).most_common()

        if len(count1) == 1 and len(count2) == 1:
            if count1[0][0] == count2[0][0]:
                return count2[0][1]
            return 0

        changes1, changes2 = 0, 0
        if count1[0][0] == count2[0][0]:
            if count2[0][1] >= count1[0][1]:
                changes2 = second - count2[0][1]
                changes1 = first - count1[1][1]
            else:
                changes2 = second - count2[1][1]
                changes1 = first - count1[0][1]
        else:
            changes2 = second - count2[0][1]
            changes1 = first - count1[0][1]

        return changes1 + changes2


solution = Solution()
assert solution.minimumOperations([3, 1, 3, 2, 4, 3]) == 3
assert solution.minimumOperations([1, 2, 2, 2, 2]) == 2
