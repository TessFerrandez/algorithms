'''
You are given a 0-indexed integer array mapping which represents the mapping rule of a shuffled decimal system. mapping[i] = j means digit i should be mapped to digit j in this system.

The mapped value of an integer is the new integer obtained by replacing each occurrence of digit i in the integer with mapping[i] for all 0 <= i <= 9.

You are also given another integer array nums. Return the array nums sorted in non-decreasing order based on the mapped values of its elements.

Notes:

Elements with the same mapped values should appear in the same relative order as in the input.
The elements of nums should only be sorted based on their mapped values and not be replaced by them.
'''
from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        translated = []
        for i, num in enumerate(nums):
            digits = list(str(num))
            new_num = ''
            for digit in digits:
                new_num += str(mapping[int(digit)])
            translated.append((i, int(new_num)))
        translated.sort(key=lambda x: x[1])
        return [nums[i] for i, j in translated]


solution = Solution()
assert solution.sortJumbled([8,9,4,0,2,1,3,5,7,6], [991,338,38]) == [338, 38, 991]
assert solution.sortJumbled([0,1,2,3,4,5,6,7,8,9], [789,456,123]) == [123, 456, 789]
