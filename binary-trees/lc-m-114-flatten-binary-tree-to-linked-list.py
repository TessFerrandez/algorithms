from typing import Optional
from TreeNode import TreeNode, deserialize, arr_from_btree


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None

        left = self.flatten(root.left)
        right = self.flatten(root.right)

        root.left = None
        root.right = left
        current = root

        while current.right:
            current = current.right

        current.right = right

        return root


solution = Solution()
assert arr_from_btree(solution.flatten(deserialize([1, 2, 5, 3, 4, None, 6]))) == [1, None, 2, None, 3, None, 4, None, 5, None, 6]
