'''
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.
'''
from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set([start])
        todo = deque([start])

        while todo:
            node = todo.popleft()
            if arr[node] == 0:
                return True

            jump = arr[node]
            if node - jump >= 0 and (node - jump) not in visited:
                visited.add(node - jump)
                todo.append(node - jump)
            if node + jump < n and (node + jump) not in visited:
                visited.add(node + jump)
                todo.append(node + jump)

        return False


solution = Solution()
assert solution.canReach([4,2,3,0,3,1,2], 5)
assert solution.canReach([4,2,3,0,3,1,2], 0)
assert not solution.canReach([3,0,2,1,2], 2)
