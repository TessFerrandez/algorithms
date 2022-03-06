'''
Given the root of a binary tree, return the sum of all left leaves.
'''
from typing import Optional
from TreeNode import TreeNode, deserialize
from collections import deque


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_sum = 0
        todo = deque([(False, root)])
        while todo:
            left, node = todo.popleft()
            if not node:
                continue
            if left and not node.left and not node.right:
                left_sum += node.val
                continue
            todo.append((True, node.left))
            todo.append((False, node.right))

        return left_sum


solution = Solution()
assert solution.sumOfLeftLeaves(deserialize([3, 9, 20, None, None, 15, 7])) == 24
assert solution.sumOfLeftLeaves(deserialize([1])) == 0
