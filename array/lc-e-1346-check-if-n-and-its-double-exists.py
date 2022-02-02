'''
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
'''
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        nums = set()

        for num in arr:
            if num * 2 in nums:
                return True
            if num % 2 == 0 and num // 2 in nums:
                return True
            nums.add(num)

        return False


solution = Solution()
assert solution.checkIfExist([10, 2, 5, 3])
assert solution.checkIfExist([7, 1, 14, 11])
assert not solution.checkIfExist([3, 1, 7, 11])
