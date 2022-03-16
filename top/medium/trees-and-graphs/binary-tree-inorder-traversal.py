from typing import Optional, List
from TreeNode import TreeNode, from_array


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


solution = Solution()
assert solution.inorderTraversal(from_array([1, None, 2, 3])) == [1, 3, 2]
assert solution.inorderTraversal(from_array([])) == []
assert solution.inorderTraversal(from_array([1])) == [1]
