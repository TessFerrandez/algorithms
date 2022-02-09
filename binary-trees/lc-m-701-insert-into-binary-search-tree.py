from typing import Optional
from TreeNode import TreeNode, create_btree, arr_from_btree


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


solution = Solution()
print(arr_from_btree(solution.insertIntoBST(create_btree([4, 2, 7, 1, 3]), 5)))
print(arr_from_btree(solution.insertIntoBST(create_btree([40, 20, 60, 10, 30, 50, 70]), 25)))
print(arr_from_btree(solution.insertIntoBST(create_btree([4, 2, 7, 1, 3, None, None, None, None, None, None]), 5)))
