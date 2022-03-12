from typing import Optional
from TreeNode import TreeNode, from_array


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):
            if not node:
                return True
            if min_val < node.val < max_val:
                return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)
            else:
                return False

        min_val, max_val = -2 ** 31 - 1, 2 ** 31
        return validate(root, min_val, max_val)


solution = Solution()
assert solution.isValidBST(from_array([2147483647]))
assert solution.isValidBST(from_array([2, 1, 3]))
assert not solution.isValidBST(from_array([2, 2, 2]))
assert not solution.isValidBST(from_array([5, 1, 4, None, None, 3, 6]))
