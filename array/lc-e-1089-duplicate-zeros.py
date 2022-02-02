'''
Duplicate all zeros in the array, and move the rest of the elements down-stream
Modify the original array
'''
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        start = 0
        while start < n - 1:
            if arr[start] == 0:
                # duplicate and move things forward
                prev = 0
                for i in range(start + 1, n):
                    arr[i], prev = prev, arr[i]
                start += 1
            start += 1


solution = Solution()

array = [1, 0, 2, 3, 0, 4, 5, 0]
solution.duplicateZeros(array)
assert array == [1, 0, 0, 2, 3, 0, 0, 4]

array = [1, 2, 3]
solution.duplicateZeros(array)
assert array == [1, 2, 3]
