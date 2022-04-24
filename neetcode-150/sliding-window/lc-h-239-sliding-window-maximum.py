from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        Ex. [1, 3, -1, -3, 5, 3, 6, 7]
        i   queue                           max
        ---------------------------------------
        0   0(1)
        1   1(3)
        2   1(3), 2(-1)                     3
        3   1(3), 2(-1), 3(-3)              3
        4   4(5)                            5
        5   4(5), 5(3)                      5
        6   6(6)                            6
        7   7(7)                            7
        '''
        queue = deque()
        result = []

        for i, num in enumerate(nums):
            while queue and nums[queue[-1]] <= num:
                queue.pop()

            queue.append(i)

            # remove the first element if it is outside the window
            if queue[0] == i - k:
                queue.popleft()

            # if window has k elements, add to results
            if i >= k - 1:
                result.append(nums[queue[0]])

        return result


solution = Solution()
assert solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3, 3, 5, 5, 6, 7]
assert solution.maxSlidingWindow([1], 1) == [1]
