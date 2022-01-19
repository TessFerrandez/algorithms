'''
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.
Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
'''
from typing import List
from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        freq = defaultdict(int)

        for num in time:
            freq[num % 60] += 1

        freq_keys = [key for key in freq]

        total_pairs = 0
        for rest in freq_keys:
            needed = 60 - rest
            if needed == 60:
                needed = 0
            if needed == rest:
                total_pairs += freq[rest] * (freq[rest] - 1)
            else:
                total_pairs += freq[rest] * freq[needed]

        return total_pairs // 2


solution = Solution()
assert solution.numPairsDivisibleBy60([30, 20, 150, 100, 40]) == 3
assert solution.numPairsDivisibleBy60([60, 60, 60]) == 3
