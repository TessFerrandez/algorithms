from heapq import heappop, heappush
from typing import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        counts = Counter(s)
        heap = []
        for c in counts:
            heappush(heap, -counts[c])

        prev_max = heappop(heap)
        deletions = 0
        while heap:
            next_max = heappop(heap)
            if next_max == prev_max:
                if next_max + 1 != 0:
                    heappush(heap, next_max + 1)
                deletions += 1
            else:
                prev_max = next_max
        return deletions


solution = Solution()
assert solution.minDeletions('aab') == 0
assert solution.minDeletions('aaabbbcc') == 2
assert solution.minDeletions('aaabbbccc') == 3
assert solution.minDeletions('ceabaacb') == 2
