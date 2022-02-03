from typing import List, Optional
from TreeNode import TreeNode, create_btree


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


solution = Solution()
assert solution.inorderTraversal(create_btree([1, None, 2, None, None, 3])) == [1, 3, 2]
assert solution.inorderTraversal(create_btree([1])) == [1]
assert solution.inorderTraversal(create_btree([])) == []
