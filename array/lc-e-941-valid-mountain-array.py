'''
Given an array of integers arr, return true if and only if it is a valid mountain array.
'''
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False

        i = 1
        while i < n and arr[i] > arr[i - 1]:
            i += 1

        if i == n or i == 1:
            return False

        while i < n and arr[i] < arr[i - 1]:
            i += 1

        if i == n:
            return True

        return False


solution = Solution()

assert solution.validMountainArray([9,8,7,6,5,4,3,2,1,0]) == False
assert solution.validMountainArray([0, 3, 2, 1]) == True
assert solution.validMountainArray([2, 1]) == False
assert solution.validMountainArray([3, 5, 5]) == False
