'''
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
'''
from typing import Optional

from TreeNode import TreeNode, create_btree


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        todo = [(0, root)]

        while todo:
            cum_sum, node = todo.pop()

            if cum_sum + node.val == targetSum and not node.left and not node.right:
                return True

            if node.left:
                todo.append((cum_sum + node.val, node.left))

            if node.right:
                todo.append((cum_sum + node.val, node.right))

        return False


solution = Solution()
assert not solution.hasPathSum(create_btree([]), 0)
assert not solution.hasPathSum(create_btree([1, 2]), 1)
assert solution.hasPathSum(create_btree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22)
assert not solution.hasPathSum(create_btree([1, 2, 3]), 5)
