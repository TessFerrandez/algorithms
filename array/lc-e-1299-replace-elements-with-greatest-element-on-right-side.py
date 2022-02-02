'''
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
'''
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1

        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]
            arr[i] = max_right
            max_right = max(max_right, current)

        return arr


solution = Solution()
assert solution.replaceElements([17, 18, 5, 4, 6, 1]) == [18, 6, 6, 6, 1, -1]
assert solution.replaceElements([400]) == [-1]
