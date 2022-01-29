'''
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.
----
Solution from StefanPochmann

Build the answer bit by bit from left to right (highest bit to lowest bit). Let's say we already know the largest first seven bits we can create. How to find the largest first eight bits we can create? Well it's that maximal seven-bits prefix followed by 0 or 1. Append 0 and then try to create the 1 one (i.e., answer ^ 1) from two eight-bits prefixes from nums. If we can, then change that 0 to 1.

Bit more explanation: answer^1 ^ p in prefixes means there's a prefix q in prefixes such that answer^1 ^ p == q. Which means p ^ q == answer ^ 1. So there are two prefixes (p and q) whose xor is answer ^ 1.
'''
from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        answer = 0
        for i in range(32)[::-1]:
            answer <<= 1
            prefixes = {num >> i for num in nums}
            answer += any(answer ^ 1 ^ p in prefixes for p in prefixes)
        return answer


solution = Solution()
assert solution.findMaximumXOR([3, 10, 5, 25, 2, 8]) == 28
assert solution.findMaximumXOR([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70])
