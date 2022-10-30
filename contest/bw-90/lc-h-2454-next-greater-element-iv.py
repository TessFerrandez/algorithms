from heapq import heappop, heappush
from typing import List


class Solution:
    # from tojuna
    def secondGreaterElement1(self, A: List[int]) -> List[int]:
        mid, stk, n = [[] for _ in range(len(A))], [], len(A)
        for i in range(n):
            while stk and A[stk[-1]] < A[i]:
                mid[i].append(stk.pop())
            stk.append(i)
        pq, ans = [], [-1] * len(A)
        for i in range(n):
            while pq and pq[0][0] < A[i]:
                ans[heappop(pq)[1]] = A[i]
            for j in mid[i]:
                heappush(pq, (A[j], j))
        return ans

    def secondGreaterElement2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        firsts = []
        seconds = [[] for _ in range(n)]

        for i, num in enumerate(nums):
            while firsts and nums[firsts[-1]] < num:
                seconds[i].append(firsts.pop())
            firsts.append(i)

        result = [-1] * n
        pq = []

        for i, num in enumerate(nums):
            while pq and pq[0][0] < num:
                result[heappop(pq)[1]] = num
            for first in seconds[i]:
                heappush(pq, (nums[first], first))

        return result

    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        needs_first, needs_second = [], []

        for i, num in enumerate(nums):
            # if we have some indices that need a second greater and this fits - we have a result
            while needs_second and nums[needs_second[-1]] < num:
                result[needs_second.pop()] = num

            # if we have some indices that need a first greater and this fits - add it to needs_second (sorted)
            tmp = []
            while needs_first and nums[needs_first[-1]] < num:
                tmp.append(needs_first.pop())
            needs_second += tmp[::-1]

            # this index doesn't have any followers yet
            needs_first.append(i)
        return result


solution = Solution()
assert solution.secondGreaterElement([2,4,0,9,6]) == [9,6,6,-1,-1]
assert solution.secondGreaterElement([3,3]) == [-1, -1]
