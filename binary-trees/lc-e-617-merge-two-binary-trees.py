from typing import List, Optional
from TreeNode import TreeNode, create_btree, arr_from_btree


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            tree = TreeNode(root1.val + root2.val)
            tree.left = self.mergeTrees(root1.left, root2.left)
            tree.right = self.mergeTrees(root1.right, root2.right)
        elif root1:
            tree = TreeNode(root1.val)
            tree.left = self.mergeTrees(root1.left, None)
            tree.right = self.mergeTrees(root1.right, None)
        elif root2:
            tree = TreeNode(root2.val)
            tree.left = self.mergeTrees(root2.left, None)
            tree.right = self.mergeTrees(root2.right, None)
        else:
            return None

        return tree


solution = Solution()
print(arr_from_btree(solution.mergeTrees(create_btree([1, 3, 2, 5], 0), create_btree([2, 1, 3, None, 4, None, 7], 0))))
print(arr_from_btree(solution.mergeTrees(create_btree([1]), create_btree([1, 2]))))
