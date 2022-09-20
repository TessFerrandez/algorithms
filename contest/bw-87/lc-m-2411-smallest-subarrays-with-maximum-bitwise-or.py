from collections import defaultdict, deque
from typing import List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        bits = defaultdict(deque)

        def mark_bits(num, idx):
            bin_num = bin(num)[2:]
            for i, val in enumerate(bin_num[::-1]):
                if val == "1":
                    bits[i].append(idx)

        for i, num in enumerate(nums):
            mark_bits(num, i)

        result = []
        for i in range(len(nums)):
            best = i
            for bit in bits:
                while bits[bit] and bits[bit][0] < i:
                    bits[bit].popleft()
                if bits[bit]:
                    best = max(best, bits[bit][0])
            result.append(best - i + 1)

        return result


solution = Solution()
assert solution.smallestSubarrays([1, 0, 2, 1, 3]) == [3,3,2,2,1]
assert solution.smallestSubarrays([1, 2]) == [2,1]
