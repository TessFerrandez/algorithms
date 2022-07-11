from typing import Optional
from TreeNode import TreeNode, deserialize


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


solution = Solution()
assert solution.maxDepth(deserialize([3,9,20,None,None,15,7])) == 3
assert solution.maxDepth(deserialize([1, None, 2])) == 2
