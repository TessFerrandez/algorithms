'''
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
'''
from typing import Optional
from TreeNode import TreeNode


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val == val:
            return root

        left = self.searchBST(root.left, val)
        if left:
            return left
        right = self.searchBST(root.right, val)
        if right:
            return right

        return None
