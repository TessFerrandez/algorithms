'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
'''
from typing import Optional
from TreeNode import TreeNode, create_btree


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and is_mirror(node1.right, node2.left) and is_mirror(node1.left, node2.right)

        return is_mirror(root, root)


solution = Solution()
assert solution.isSymmetric(create_btree([1, 2, 2, 3, 4, 4, 3]))
assert not solution.isSymmetric(create_btree([1, 2, 2, None, 3, None, 3]))
assert not solution.isSymmetric(create_btree([1, 2, 2, 2, None, 2]))
