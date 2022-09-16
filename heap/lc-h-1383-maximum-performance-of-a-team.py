from heapq import heappop, heappush
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = list(zip(efficiency, speed))
        engineers.sort(reverse=True)

        best_team = 0
        current_sum = 0
        heap = []
        for e, s in engineers:
            current_sum += s
            heappush(heap, s)

            if len(heap) > k:
                current_sum -= heappop(heap)

            best_team = max(best_team, current_sum * e)

        return best_team % (10 ** 9 + 7)


solution = Solution()
assert solution.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2) == 60
assert solution.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3) == 68
assert solution.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 4) == 72
