from typing import List
from collections import deque


class MonoQueue:
    def __init__(self) -> None:
        self.mqueue = deque([])

    def push(self, val):
        count = 0
        while self.mqueue and self.mqueue[-1][0] < val:
            count += self.mqueue[-1][1] + 1
            self.mqueue.pop()
        self.mqueue.append([val, count])

    def get_max(self):
        return self.mqueue[0][0]

    def pop(self):
        if self.mqueue[0][1] > 0:
            self.mqueue[0][1] -= 1
            return
        self.mqueue.popleft()


class Solution:
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        results = []
        mq = MonoQueue()
        k = min(k, len(nums))

        i = 0
        while i < k - 1:
            mq.push(nums[i])
            i += 1

        while i < len(nums):
            mq.push(nums[i])
            results.append(mq.get_max())
            mq.pop()
            i += 1

        return results

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        result = []

        for i, current in enumerate(nums):
            while q and nums[q[-1]] <= current:
                q.pop()
            q.append(i)

            # remove first if it is outside the window
            if q[0] == i - k:
                q.popleft()
            # if window has k elements, add to results
            if i >= k - 1:
                result.append(nums[q[0]])

        return result


solution = Solution()
assert solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
assert solution.maxSlidingWindow([1], 1) == [1]
