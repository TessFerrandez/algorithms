'''
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
'''
from typing import Optional
from TreeNode import TreeNode, deserialize


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return inorder(root)[k - 1]


solution = Solution()
assert solution.kthSmallest(deserialize([3, 1, 4, None, 2]), 1) == 1
assert solution.kthSmallest(deserialize([5, 3, 6, 2, 4, None, None, 1]), 3) == 3
