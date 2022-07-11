from math import inf
from typing import Optional
from TreeNode import TreeNode, deserialize


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(node, min_val, max_val):
            if not node:
                return True
            if node.val < min_val or node.val > max_val:
                return False
            return is_valid(node.left, min_val, node.val - 1) and is_valid(node.right, node.val + 1, max_val)

        if not root:
            return True

        return is_valid(root, -inf, inf)


solution = Solution()
assert solution.isValidBST(deserialize([2, 1, 3]))
assert not solution.isValidBST(deserialize([5, 1, 4, None, None, 3, 6]))
assert not solution.isValidBST(deserialize([5, 4, 6, None, None, 3, 7]))
