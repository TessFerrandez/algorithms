# array, two pointers, binary search
from bisect import bisect_left
from typing import List


class Solution:
    # solution with hash table
    def twoSum_hash(self, numbers: List[int], target: int) -> List[int]:
        # until num is greater than target
        # check if target - num is in the list
        lower_numbers = {}
        lowest_num = numbers[0]

        for i, num in enumerate(numbers):
            if num > target - lowest_num:
                break
            if target - num in lower_numbers:
                return [lower_numbers[target - num], i + 1]
            lower_numbers[num] = i + 1

    # solution with binary search
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            # binary search for the target - num
            j = bisect_left(numbers, target - num, i + 1)
            if j < len(numbers) and numbers[j] == target - num:
                return [i + 1, j + 1]

solution = Solution()
assert solution.twoSum([2, 7, 11, 15], 9) == [1, 2]
assert solution.twoSum([2, 3, 4], 6) == [1, 3]
assert solution.twoSum([-1, 0], -1) == [1, 2]
