'''
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.
'''
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        sub_len = 1

        total = 0
        while sub_len <= n:
            for i in range(n - sub_len + 1):
                print(arr[i: i + sub_len])
                total += sum(arr[i: i + sub_len])
            sub_len += 2

        return total


solution = Solution()
assert solution.sumOddLengthSubarrays([1, 4, 2, 5, 3]) == 58
assert solution.sumOddLengthSubarrays([1, 2]) == 3
