from heapq import heappop, heappush
from typing import List


class Solution:
    # using max heap - O(M*N*logK)/O(k)
    def kthSmallest1(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        max_heap = []

        for row in range(n):
            for col in range(n):
                heappush(max_heap, -matrix[row][col])
                if len(max_heap) > k:
                    heappop(max_heap)

        return -heappop(max_heap)

    # using min heap - O(k * log k)/O(k)
    def kthSmallest2(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []   # (val, r, c)
        for r in range(min(k, n)):
            heappush(min_heap, (matrix[r][0], r, 0))

        answer = -1
        for _ in range(k):
            answer, r, c = heappop(min_heap)
            if c + 1 < n:
                heappush(min_heap, (matrix[r][c + 1], r, c + 1))

        return answer

    # binary search - O((n + n) * log d) / O(1) -- d = max_elem - min_elem
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def count_less_or_equal(x):
            count = 0
            col = n - 1
            for row in range(n):
                while col >= 0 and matrix[row][col] > x:
                    col -= 1
                count += (col + 1)
            return count

        left, right = matrix[0][0], matrix[-1][-1]
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            if count_less_or_equal(mid) >= k:
                answer = mid
                right = mid - 1
            else:
                left = mid + 1

        return answer


solution = Solution()
assert solution.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8) == 13
assert solution.kthSmallest([[-5]], 1) == -5
