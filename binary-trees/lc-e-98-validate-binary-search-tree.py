'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
from typing import Optional
from TreeNode import TreeNode, create_btree


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, min_val, max_val):
            if not root:
                return True

            if not min_val < root.val < max_val:
                return False

            return validate(root.left, min_val, root.val) and validate(root.right, root.val, max_val)

        return validate(root, -2 ** 31 - 1, 2 ** 31)


solution = Solution()
assert solution.isValidBST(create_btree([2147483647]))
assert not solution.isValidBST(create_btree([5, 4, 6, None, None, 3, 7]))
assert solution.isValidBST(create_btree([2, 1, 3]))
assert not solution.isValidBST(create_btree([2, 2, 2]))
assert not solution.isValidBST(create_btree([5, 1, 4, None, None, 3, 6]))
