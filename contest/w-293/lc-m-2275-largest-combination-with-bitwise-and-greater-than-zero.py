'''
16    10000
17    10001
71  1000111
62   111110
12     1100
24    11000
14     1110

0   - 17, 71
1   - 71, 62
2   - 71, 62, 12, 14
3   - 62, 12, 14
4   - 16, 17, 62, 24
5   - 62
6   - 71
'''
from collections import defaultdict
from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bits = defaultdict(int)

        for candidate in candidates:
            for bit in range(25):
                if candidate & 1 << bit != 0:
                    bits[bit] += 1

        return max(bits.values())


solution = Solution()
assert solution.largestCombination([16,17,71,62,12,24,14]) == 4
assert solution.largestCombination([8, 8]) == 2
