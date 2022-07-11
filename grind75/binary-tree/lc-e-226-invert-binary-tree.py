from typing import Optional
from TreeNode import TreeNode, serialize, deserialize


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root


solution = Solution()
assert not solution.invertTree(None)
assert serialize(solution.invertTree(deserialize([2, 1, 3]))) == [2, 3, 1]
assert serialize(solution.invertTree(deserialize([4,2,7,1,3,6,9]))) == [4,7,2,9,6,3,1]
