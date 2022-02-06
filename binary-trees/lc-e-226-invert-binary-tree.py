'''
Given the root of a binary tree, invert the tree, and return its root.
'''
from typing import Optional
from TreeNode import TreeNode, create_btree, arr_from_btree


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


solution = Solution()

root = create_btree([4, 2, 7, 1, 3, 6, 9])
assert arr_from_btree(solution.invertTree(root)) == [4, 7, 2, 9, 6, 3, 1]

root = create_btree([2, 1, 3])
assert arr_from_btree(solution.invertTree(root)) == [2, 3, 1]

root = create_btree([])
assert arr_from_btree(solution.invertTree(root)) == []
