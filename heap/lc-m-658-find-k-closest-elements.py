from heapq import heappop, heappush
from typing import List


class Solution:
    # my solution
    def findClosestElements2(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for num in arr:
            heappush(heap, (abs(num - x), num))

        result = []
        for _ in range(k):
            _, num = heappop(heap)
            result.append(num)

        result.sort()
        return result

    # more optimized bin search solution
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k

        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left: left + k]


solution = Solution()
assert solution.findClosestElements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]
assert solution.findClosestElements([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]
