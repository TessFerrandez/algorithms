from typing import List, Optional
from TreeNode import TreeNode, create_btree


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


solution = Solution()
assert solution.preorderTraversal(create_btree([1, None, 2, None, None, 3])) == [1, 2, 3]
assert solution.preorderTraversal(create_btree([1])) == [1]
assert solution.preorderTraversal(create_btree([])) == []
