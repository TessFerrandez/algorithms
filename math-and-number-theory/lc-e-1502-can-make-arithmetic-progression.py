'''
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.
'''
from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) == 2:
            return True

        arr.sort()
        diff = arr[1] - arr[0]
        current = arr[1]

        for num in arr[2:]:
            if (num - current) != diff:
                return False
            current = num

        return True


solution = Solution()
assert solution.canMakeArithmeticProgression([-68,-96,-12,-40,16])
assert solution.canMakeArithmeticProgression([3, 5, 1])
assert not solution.canMakeArithmeticProgression([1, 2, 4])
