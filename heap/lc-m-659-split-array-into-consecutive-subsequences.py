from collections import Counter
from heapq import heappop, heappush
from typing import List


class Solution:
    def isPossible1(self, nums: List[int]) -> bool:
        remaining = Counter(nums)
        ends_in = Counter()
        for num in nums:
            if not remaining[num]:
                continue
            remaining[num] -= 1
            if ends_in[num - 1] > 0:
                ends_in[num - 1] -= 1
                ends_in[num] += 1
            elif remaining[num + 1] and remaining[num + 2]:
                remaining[num + 1] -= 1
                remaining[num + 2] -= 1
                ends_in[num + 2] += 1
            else:
                return False
        return True

    def isPossible(self, nums: List[int]) -> bool:
        heap = []   # end, length

        for num in nums:
            while heap and heap[0][0] + 1 < num:
                _, length = heappop(heap)
                if length < 3:
                    return False
            if not heap or heap[0][0] == num:
                heappush(heap, (num, 1))
            else:
                _, length = heappop(heap)
                heappush(heap, (num, length + 1))

        while heap:
            _, length = heappop(heap)
            if length < 3:
                return False

        return True


solution = Solution()
assert solution.isPossible([1,2,3,3,4,5])
assert solution.isPossible([1,2,3,3,4,4,5,5])
assert not solution.isPossible([1,2,3,4,4,5])
