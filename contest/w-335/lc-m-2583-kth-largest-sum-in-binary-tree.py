from collections import deque
from heapq import heappop, heappush
from typing import Optional
from TreeNode import TreeNode, deserialize


class Solution:
    def kthLargestLevelSum_my(self, root: Optional[TreeNode], k: int) -> int:
        current_level = [root]
        sums = []

        while current_level:
            current_sum = sum(node.val for node in current_level if node)
            if current_sum > 0:
                sums.append(current_sum)
            next_level = []
            for node in current_level:
                if node:
                    next_level.append(node.left)
                    next_level.append(node.right)
            current_level = next_level

        if len(sums) < k:
            return -1
        sums.sort()
        return sums[-k]

    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        todo = deque([root])
        sums = []

        while todo:
            nodes_in_level = len(todo)
            level_sum = 0

            for _ in range(nodes_in_level):
                node = todo.popleft()
                level_sum += node.val
                if node.left:
                    todo.append(node.left)
                if node.right:
                    todo.append(node.right)

            heappush(sums, -level_sum)

        if len(sums) < k:
            return -1
        for _ in range(k - 1):
            heappop(sums)
        return -sums[0]


solution = Solution()
assert solution.kthLargestLevelSum(deserialize([5,8,9,2,1,3,7]), 4) == -1
assert solution.kthLargestLevelSum(deserialize([5,8,9,2,1,3,7,4,6]), 2) == 13
assert solution.kthLargestLevelSum(deserialize([1,2,None,3]), 1) == 3
