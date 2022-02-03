from typing import List, Optional
from TreeNode import TreeNode, create_btree


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]


solution = Solution()
assert solution.postorderTraversal(create_btree([1, None, 2, None, None, 3])) == [3, 2, 1]
assert solution.postorderTraversal(create_btree([1])) == [1]
assert solution.postorderTraversal(create_btree([])) == []
