'''

'''
from math import lcm, gcd
from typing import List


class Solution:
    # TLE
    def replaceNonCoprimes2(self, nums: List[int]) -> List[int]:
        def is_coprime(x, y):
            return gcd(x, y) == 1

        def find_non_coprime(nums):
            for i in range(len(nums) - 1):
                if is_coprime(nums[i], nums[i + 1]):
                    continue
                return i
            return -1

        while True:
            i = find_non_coprime(nums)
            if i != -1:
                p1, p2 = nums[i], nums[i + 1]
                nums[i + 1] = lcm(p1, p2)
                nums = nums[:i] + nums[i + 1:]
            else:
                return nums

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums

        stack = []
        for num in nums:
            stack.append(num)
            while len(stack) > 1 and (gcd_ := gcd(stack[-1], stack[-2])) > 1:
                last = stack.pop()
                stack[-1] = stack[-1] * last // gcd_

        return stack


solution = Solution()
assert solution.replaceNonCoprimes([6, 4, 3, 2, 7, 6, 2]) == [12, 7, 6]
assert solution.replaceNonCoprimes([2, 2, 1, 1, 3, 3, 3]) == [2, 1, 1, 3]
