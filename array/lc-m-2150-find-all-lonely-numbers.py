'''
You are given an integer array nums. A number x is lonely when it appears only once, and no adjacent numbers (i.e. x + 1 and x - 1) appear in the array.

Return all lonely numbers in nums. You may return the answer in any order.
'''
from typing import List
from collections import Counter


class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)

        single = [num for num in counts if counts[num] == 1]
        result = []
        for num in single:
            if num + 1 not in counts and num - 1 not in counts:
                result.append(num)
        return result


solution = Solution()
assert solution.findLonely([10,6,5,8]) == [10, 8]
assert solution.findLonely([1,3,5,3]) == [1, 5]